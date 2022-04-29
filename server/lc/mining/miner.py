from typing import Callable
import random

from lc.blockchain.block.block import Block
from lc.util.info import mining_info as info
from lc.util import colors
from lc.blockchain.block.block_header import BlockHeader
from lc.blockchain.blockchain import GENESIS_HASH

from lc.util.conversions import int_to_bytes
from lc.cryptography import puzzle

class Miner:
    def __init__(
        self,
        # Should return a reference to the latest block in the chain, or None if chain is empty
        get_latest_block: Callable[[], Block],
        # Should add provided block to chain
        add_block_to_chain: Callable[[Block], None],
        # Should trigger a broadcast of the chain to the network
        trigger_broadcast: Callable[[], None]
        ):
        self.get_latest_block = get_latest_block
        self.add_block_to_chain = add_block_to_chain
        self.trigger_broadcast = trigger_broadcast

        self.is_mining = False

        self.current_block = None
        self.current_block_changed = False

    def mine(self):
        self.is_mining = True
        info('Beginning mining...')

        while True:
            last_block = self.get_latest_block()

            if last_block is None:
                # Chain is empty, create genesis block
                self.current_block = Block(BlockHeader(GENESIS_HASH))
            else:
                # Otherwise, the new block we mine has the last proven block's hash in its header
                self.current_block = Block(BlockHeader(last_block.to_puzzle_hash()))
            
            info(f'Starting proof of block with {len(self.current_block.transactions)} transactions.')

            # === Prove the block ===
            if self.prove(self.current_block):
                # Add our newly proven block to our local chain
                self.add_block_to_chain(self.current_block)

                # Broadcast the (theoretically) new longest chain
                #communication.broadcast_chain(chain)
                self.trigger_broadcast()

                # Create a new block to prove
                self.current_block = Block(BlockHeader(self.current_block.to_puzzle_hash()))
            else:
                # Get hash of newest received block
                #new_block = Block(BlockHeader(chain.blocks[-1].to_puzzle_hash()))
                self.current_block = Block(BlockHeader(self.get_latest_block().to_puzzle_hash()))


    def prove(self, block: Block) -> bool:
        # Returns true if block was proven or false if interrupted (i.e. detected a change in the chain)
        # Start at random value
        proof = random.randrange(0, 1_000_000)

        # Cached block hash
        current_block_hash = block.to_puzzle_hash()

        while True:
            if self.current_block_changed:
                # Recompute block hash if needed
                info(f'Received new transaction, now mining block with {len(self.current_block.transactions)} transactions')
                current_block_hash = block.to_puzzle_hash()
                self.current_block_changed = False

            #if len(chain) > init_chain_len:

            # TODO: improve below speed
            # Make sure latest block not None and then check if hashes match
            if self.get_latest_block() and block.header.previous_block_hash != self.get_latest_block().to_puzzle_hash():
                info(f'Detected updated chain, interrupting proof of block.')
                return False

            if puzzle.is_valid_proof(current_block_hash, int_to_bytes(proof)):
                info(f'{colors.GREEN}Proof found{colors.RESET} with integer value: {proof} ({int_to_bytes(proof).hex()})')
                block.header.proof = int_to_bytes(proof)
                return True
            # Increment proof
            proof += 1