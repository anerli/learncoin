from block import Block, BlockHeader
from chain import GENESIS_HASH, BlockChain
#from chain_manager import chain
import communication
from time import time
from conversions import int_to_bytes
import puzzle
import colors
import random

def info(*args, **kwargs):
    print(f'{colors.YELLOW}<MINING>{colors.RESET}', *args, **kwargs)

def mine(chain):
    #global chain
    info('Beginning mining...')
    '''
    Repeatedly mine on chain.
    '''
    while True:
        # === Create genesis block or get current block ===
        if len(chain) == 0:
            # Genesis block
            block = Block(BlockHeader(GENESIS_HASH))

        # === Prove the block ===
        if prove(block, chain):
            # Add our newly proven block to our local chain
            chain.add_block(block)

            # Broadcast the (theoretically) new longest chain
            communication.broadcast_chain(chain)

            # Create a new block to prove
            block = Block(BlockHeader(block.to_puzzle_hash()))
        else:
            # Get hash of newest received block
            block = Block(BlockHeader(chain.blocks[-1].to_puzzle_hash()))

def prove(block: Block, chain: BlockChain) -> bool:
    #global chain
    # Returns true if block was proven or false if interrupted
    # Start at random value
    proof = random.randrange(0, 1_000_000)
    #start = time()
    # TODO: Need to get a signal for when chain is replaced so we can stop mining this block

    current_block_hash = block.to_puzzle_hash()

    init_chain_len = len(chain)
    #print('===== LAST CHAIN LEN: ', init_chain_len)

    while True:
        #if proof % 100000 == 0: print(f'{len(chain)=}, {init_chain_len=}')
        if len(chain) > init_chain_len:
            info(f'Detected updated chain, interrupting proof of block.')
            return False
        #if proof % DEBUG_INTERVAL == 0: print('Trying proof:', proof)
        if puzzle.is_valid_proof(current_block_hash, int_to_bytes(proof)):
            info(f'Proof found: {proof}')
            block.header.proof = int_to_bytes(proof)
            return True
        # Increment proof
        proof += 1
    #print(f'<MINING> Proof found: {proof}')
    #print(f'<MINING> Time to prove: {time() - start} seconds.')
    
    #info(f'<MINING> Time to prove: {time() - start} seconds.')

    # Add proof to block header
    

    #print(f'Is block valid? {block.is_valid()}')
