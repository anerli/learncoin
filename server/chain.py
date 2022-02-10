from block import Block, BlockHeader

from typing import List

# Constant value representing the hash of an imaginary genesis block
GENESIS_HASH = b"this is the UTF-8 representation of the genesis hash bytes"

class BlockChain:
    def __init__(self, blocks: List[Block] = []):
        pass
    
    def to_json(self) -> dict:
        pass
    
    def add_block(self, block: Block):
        if not block.is_valid():
            raise Exception("Attempted to add invalid block to chain!")
    
    def is_valid(self):
        # Verify all blocks as a proof chain

        last_hash = GENESIS_HASH

        for block in self.blocks:
            if block.header.previous_block_hash != last_hash:
                return False
            if not block.is_valid():
                return False
        
        # If all blocks and prev hashes are valid, the chain is valid
        return True