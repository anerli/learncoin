from lc.blockchain.block.block import Block
from lc.blockchain.block.block_header import BlockHeader
from lc.blockchain.blockchain import GENESIS_HASH, BlockChain
from lc.comms import communication
from lc.util.conversions import float_from_bytes, int_to_bytes
from lc.cryptography import puzzle
import random
#from lc.blockchain.chain_manager import make_transaction
#from lc.transactions.transaction_logic import make_transaction

from lc.util.info import mining_info as info
from lc.util import colors


is_mining = False
current_block = None
current_block_changed = False
chain = None

def mine(server_chain: 'BlockChain'):
    global is_mining, current_block, chain
    chain = server_chain
    is_mining = True
    #global chain
    info('Beginning mining...')
    '''
    Repeatedly mine on chain.
    '''
    while True:
        # === Create genesis block or get current block ===
        if len(chain) == 0:
            # Genesis block
            current_block = Block(BlockHeader(GENESIS_HASH))
        else:
            current_block = Block(BlockHeader(chain.blocks[-1].to_puzzle_hash()))
        
        info(f'Starting proof of block with {len(current_block.transactions)} transactions.')

        # === Prove the block ===
        if prove(current_block, chain):
            # Add our newly proven block to our local chain
            chain.add_block(current_block)

            # Broadcast the (theoretically) new longest chain
            communication.broadcast_chain(chain)

            # Create a new block to prove
            current_block = Block(BlockHeader(current_block.to_puzzle_hash()))
        else:
            # Get hash of newest received block
            current_block = Block(BlockHeader(chain.blocks[-1].to_puzzle_hash()))

def prove(block: Block, chain: BlockChain) -> bool:
    # Returns true if block was proven or false if interrupted (i.e. detected a change in the chain)
    # Start at random value
    global current_block_changed

    proof = random.randrange(0, 1_000_000)

    # Cached block hash
    current_block_hash = block.to_puzzle_hash()

    init_chain_len = len(chain)

    while True:
        if current_block_changed:
            # Recompute block hash if needed
            current_block_hash = block.to_puzzle_hash()
            current_block_changed = False

        if len(chain) > init_chain_len:
            info(f'Detected updated chain, interrupting proof of block.')
            return False

        if puzzle.is_valid_proof(current_block_hash, int_to_bytes(proof)):
            info(f'{colors.GREEN}Proof found{colors.RESET} with integer value: {proof} ({int_to_bytes(proof).hex()})')
            block.header.proof = int_to_bytes(proof)
            return True
        # Increment proof
        proof += 1

def make_transaction(transaction: 'Transaction'):

    # TODO: move this?
    '''
    Make a transaction by adding it to the latest block and notifying neighbors of it.
    Called by transaction endpoint as well as miner when a block is mined.
    '''
    global chain, current_block_changed

    if is_mining:
        global current_block
        print(current_block)
        # add to current block
        current_block.add_transaction(transaction)
        current_block_changed = True
        info(f'Received new transaction, now mining block with {len(current_block.transactions)} transactions')
        #info(current_block.transactions)
    
        #info('Is block valid?', current_block.is_valid())

    # Either way, broadcast it
    communication.broadcast_transaction(transaction)