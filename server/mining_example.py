from block import Block, BlockHeader
from chain import BlockChain, GENESIS_HASH
from conversions import int_to_bytes

import puzzle

from time import time



# Reduce difficulty for testing purposes
puzzle.DIFFICULTY = 4

DEBUG_INTERVAL = 10000

# Make new block without proof, no transactions
#b = Block(BlockHeader(GENESIS_HASH))


current_block = Block(BlockHeader(GENESIS_HASH))
chain = BlockChain()

try:
    while True:
        # Try to prove block
        proof = 0
        start = time()
        #current_block = chain.blocks[-1]
        current_block_hash = current_block.to_puzzle_hash()

        while True:
            #if proof % DEBUG_INTERVAL == 0: print('Trying proof:', proof)
            if puzzle.is_valid_proof(current_block_hash, int_to_bytes(proof)):
                break
            # Increment proof
            proof += 1
        print(f'Proof found: {proof}')
        print(f'Time to prove: {time() - start}')

        # Add proof to block header
        current_block.header.proof = int_to_bytes(proof)

        print(f'Is block valid? {current_block.is_valid()}')

        # Add a new block to prove
        chain.add_block(current_block)
        # Set up a new block to prove
        current_block = Block(BlockHeader(current_block_hash))
except KeyboardInterrupt:
    print(f'Is chain valid? {chain.is_valid()}')

    #print(chain.blocks)

    print('Chain:\n' + chain.__repr__())