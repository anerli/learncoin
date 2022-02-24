from block import Block, BlockHeader
from chain import GENESIS_HASH, BlockChain
from chain_manager import chain
import communication
from time import time
from conversions import int_to_bytes
import puzzle
import colors

def info(*args, **kwargs):
    print(f'{colors.YELLOW}<MINING>{colors.RESET}', *args, **kwargs)

def mine():
    global chain
    '''
    Repeatedly mine.
    '''
    while True:
        # === Create genesis block or get current block ===
        if len(chain) == 0:
            # Genesis block
            block = Block(BlockHeader(GENESIS_HASH))

        # === Prove the block ===
        prove(block)

        # Add our newly proven block to our local chain
        chain.add_block(block)

        # Broadcast the (theoretically) new longest chain
        communication.broadcast_chain(chain)

        # Create a new block to prove
        block = Block(BlockHeader(block.to_puzzle_hash()))

def prove(block: Block):
    proof = 0
    #start = time()

    current_block_hash = block.to_puzzle_hash()

    while True:
        #if proof % DEBUG_INTERVAL == 0: print('Trying proof:', proof)
        if puzzle.is_valid_proof(current_block_hash, int_to_bytes(proof)):
            break
        # Increment proof
        proof += 1
    #print(f'<MINING> Proof found: {proof}')
    #print(f'<MINING> Time to prove: {time() - start} seconds.')
    info(f'Proof found: {proof}')
    #info(f'<MINING> Time to prove: {time() - start} seconds.')

    # Add proof to block header
    block.header.proof = int_to_bytes(proof)

    #print(f'Is block valid? {block.is_valid()}')
