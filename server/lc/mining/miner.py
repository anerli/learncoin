from lc.blockchain.block.block import Block
from lc.blockchain.block.block_header import BlockHeader
from lc.blockchain.blockchain import GENESIS_HASH, BlockChain
from lc.comms import communication
from lc.util.conversions import int_to_bytes
from lc.cryptography import puzzle
import random

from lc.util.info import mining_info as info
from lc.util import colors


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
        info(f'Starting proof of block with {len(block.transactions)} transactions.')

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
    # Returns true if block was proven or false if interrupted (i.e. detected a change in the chain)
    # Start at random value
    proof = random.randrange(0, 1_000_000)

    current_block_hash = block.to_puzzle_hash()

    init_chain_len = len(chain)

    while True:
        #if proof % 100000 == 0: print(f'{len(chain)=}, {init_chain_len=}')
        if len(chain) > init_chain_len:
            info(f'Detected updated chain, interrupting proof of block.')
            return False
        #if proof % DEBUG_INTERVAL == 0: print('Trying proof:', proof)
        if puzzle.is_valid_proof(current_block_hash, int_to_bytes(proof)):
            info(f'{colors.GREEN}Proof found{colors.RESET} with integer value: {proof}')
            block.header.proof = int_to_bytes(proof)
            return True
        # Increment proof
        proof += 1
