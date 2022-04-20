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
            info('Just proven:', current_block)
            info(id(current_block))
            # Add our newly proven block to our local chain
            chain.add_block(current_block)

            # Broadcast the (theoretically) new longest chain
            communication.broadcast_chain(chain)

            # Create a new block to prove
            current_block = Block(BlockHeader(current_block.to_puzzle_hash()))
            print('new block', current_block) #! wh is new block not new???????????????
            info(id(current_block))
        else:
            # Get hash of newest received block
            current_block = Block(BlockHeader(chain.blocks[-1].to_puzzle_hash()))

def prove(block: Block, chain: BlockChain) -> bool:
    # Returns true if block was proven or false if interrupted (i.e. detected a change in the chain)
    # Start at random value
    proof = random.randrange(0, 1_000_000)

    #!!!!! PROBLEM: current block hash is cached!
    #current_block_hash = block.to_puzzle_hash()

    init_chain_len = len(chain)

    i = 0
    while True:
        if i % 50000 == 0: info('Trying to prove block with transactions:', block.transactions)
        i+=1
        #if proof % 100000 == 0: print(f'{len(chain)=}, {init_chain_len=}')
        if len(chain) > init_chain_len:
            info(f'Detected updated chain, interrupting proof of block.')
            return False
        #if proof % DEBUG_INTERVAL == 0: print('Trying proof:', proof)

        # ! TMP: do not cache, but this is slow!
        if puzzle.is_valid_proof(block.to_puzzle_hash(), int_to_bytes(proof)):#!
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
    global chain
    # info(f'Making transaction:')
    # print(f'\tsender: {transaction.sender.hex()}')
    # print(f'\treceiver: {transaction.receiver.hex()}')
    # print(f'\tamount: {float_from_bytes(transaction.amount)}')
    # print(f'\tsignature: {transaction.signature.hex()}')
    # info(f'Is valid? {transaction.is_valid()}')

    if is_mining:
        global current_block
        print(current_block)
        # add to current block
        current_block.add_transaction(transaction)
        info(current_block.transactions)
    
        info('Is block valid?', current_block.is_valid())

    # Either way, broadcast it
    communication.broadcast_transaction(transaction)
