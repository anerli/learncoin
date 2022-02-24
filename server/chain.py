from block import Block, BlockHeader

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
    
    def is_valid(self):
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