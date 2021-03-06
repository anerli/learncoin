from lc.blockchain.block.block import Block
from lc.blockchain.block.block_header import BlockHeader

from typing import List

# Constant value representing the hash of an imaginary genesis block
GENESIS_HASH = b"this is the UTF-8 representation of the genesis hash bytes"

class BlockChain:
    '''
    All blocks contained in this should be proven already.
    New blocks should be stored separately and added only when proven.
    '''
    def __init__(self, blocks: List[Block] = []):
        #if blocks == []:
        #    blocks.append(Block(BlockHeader(GENESIS_HASH)))
        # Actually don't add a block yet because it won't be proven
        self.blocks = blocks
    
    def __repr__(self):
        s = ''
        s += '<BlockChain\n'
        for block in self.blocks:
            s += block.__repr__() + '\n'
        s += '>\n'
        return s
    
    def describe(self):
        return f'Blockchain of length {len(self)} which is {"" if self.is_valid() else "NOT "}valid.'
    
    def __len__(self):
        return len(self.blocks)
    
    def to_json(self) -> dict:
        #return self.__dict__
        return {
            'blocks': [block.to_json() for block in self.blocks]
        }
    
    def replace(self, other: 'BlockChain'):
        # Useful for replacing local chain without replacing the chain reference itself.
        # Note that this copies the REFERENCES of the other's blocks, does not copy the actual blocks
        self.blocks = other.blocks
    
    @classmethod
    def from_json(cls, data: dict) -> 'BlockChain':
        return BlockChain(
            blocks=[Block.from_json(block) for block in data['blocks']]
        )
    
    def add_block(self, block: Block):
        # TODO: (Design) should unproven blocks be allowed on the chain object or not?
        # -> Not? Makes it less clear when comparing chain lengths
        if not block.is_valid():
           raise Exception("Attempted to add invalid block to chain!")
        self.blocks.append(block)
    
    def is_valid(self) -> bool:
        # Verify all blocks as a proof chain

        last_hash = GENESIS_HASH

        for block in self.blocks:
            if block.header.previous_block_hash != last_hash:
                #print(f'Block stored previous hash {block.header.previous_block_hash} does not match ')
                return False
            if not block.is_valid():
                return False
            last_hash = block.to_puzzle_hash()
        
        # If all blocks and prev hashes are valid, the chain is valid
        return True
    
    def calculate_addr_totals(self) -> dict:
        # Calculate the total balance of each public key address
        # Not particularly efficient
        # TODO: Should cache previous results and accumulate totals
        totals = {}
        for block in self.blocks:
            #for transaction in block.transactions:
            block_totals = block.calculate_addr_totals()
            for k, v in block_totals.items():
                if k not in totals:
                    totals[k] = v
                else:
                    totals[k] += v
        return totals
    
    def get_balance(self, pubkey: str) -> float:
        # Get balance of hex addr
        balances = self.calculate_addr_totals()
        if pubkey not in balances:
            balance = 0.0
        else:
            balance = balances[pubkey]
        return balance#json({'balance': balance})