from block import Block, BlockHeader
from chain import GENESIS_HASH, BlockChain
from chain_manager import chain
import communication
from time import time
from conversions import int_to_bytes
import puzzle

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
        #else:
        #    block = chain.blocks[-1]

        # === Prove the block ===
        #proof = find_proof(block)
        prove(block)

        # Add our newly proven block to our local chain
        chain.add_block(block)

        print('Is chain valid?', chain.is_valid())

        # Broadcast the (theoretically) new longest chain
        communication.broadcast_chain(chain)

        # Add a new block to prove
        # hmm but we can't add invalid blocks FIXME
        #chain.add_block(Block(BlockHeader(block.to_puzzle_hash())))
        block = Block(BlockHeader(block.to_puzzle_hash()))



#def next_block() -> Block:

def prove(block: Block):# -> bytes:
    proof = 0
    start = time()
    #current_block = chain.blocks[-1]
    current_block_hash = block.to_puzzle_hash()

    while True:
        #if proof % DEBUG_INTERVAL == 0: print('Trying proof:', proof)
        if puzzle.is_valid_proof(current_block_hash, int_to_bytes(proof)):
            break
        # Increment proof
        proof += 1
    print(f'Proof found: {proof}')
    print(f'Time to prove: {time() - start}')

    # Add proof to block header
    block.header.proof = int_to_bytes(proof)

    print(f'Is block valid? {block.is_valid()}')
    #return int_to_bytes(proof)
