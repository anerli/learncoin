from threading import Thread
from typing import List
from sanic import Sanic
from sanic_cors import CORS, cross_origin
from lc.blockchain.blockchain import BlockChain

from lc.discovery import DiscoveryComponent

from lc.endpoints import chain_endpoints, discovery_endpoints, test_endpoints, transactions_endpoints

import time

from lc.mining.miner import Miner
from lc.transactions.transaction import Transaction

from lc.util.info import server_info as info


class Node:
    def __init__(self, pub_addr: str, initial_neighbors: List[str], mine: bool, mining_key: str):
        # FIXME: Happens twice for some reason?
        print('Initializing node...')
        self.app = Sanic("learncoin_full_node")

        #!fixme: potential security issues for sure

        # Hack to disable annoying CORS logging
        CORS.log = lambda *args, **kwargs: None
        CORS(self.app, resources={r"/*": {"origins": "*"}})
        #self.pub_addr = pub_addr
        #self.neighbors = initial_neighbors
        self.mine = mine

        self.dc = DiscoveryComponent(pub_addr, initial_neighbors)

        self.chain = BlockChain()

        # Create miner whether or not we use it
        self.miner = Miner(
            lambda: self.chain.blocks[-1] if self.chain.blocks else None,
            lambda block: self.chain.blocks.append(block),
            lambda: self.dc.broadcast_chain(self.chain.to_json()),
            mining_key
        )
        # Used if not mining to store pending transactions
        self.pending_transactions = []

        self.app.blueprint(test_endpoints.bind(self))
        self.app.blueprint(discovery_endpoints.bind(self.dc))
        self.app.blueprint(chain_endpoints.bind(self))
        self.app.blueprint(transactions_endpoints.bind(self))

        # CORS crap
        # def add_cors_headers(response, methods):
        #     response.headers.extend({
        #         "Access-Control-Allow-Origin": "*",
        #     })
        
        # self.app.register_middleware(add_cors_headers, "response")
        

        # For ensuring we don't infinitely bounce transactions
        self.seen_transaction_hashes = set()
    
    def start_mining(self):
        # Make sure server is running before we start mining
        while not self.app.is_running:
            time.sleep(1)
        
        self.miner.mine()
    
    def check_neighbors(self):
        while not self.app.is_running:
            time.sleep(1)
        self.dc.monitor_neighbors()

    def run(self, *args, **kwargs):
        @self.app.after_server_start
        async def l1(app, loop):
            #print('L1')
            discover_thread = Thread(target=self.dc.discover_more_neighbors)
            discover_thread.daemon = True
            discover_thread.start()
            #self.dc.discover_more_neighbors()
        
        @self.app.after_server_start
        async def l2(app, loop):
            #print('L2')
            if self.mine:
                mining_thread = Thread(target=self.miner.mine)
                mining_thread.daemon = True
                mining_thread.start()
            
        @self.app.after_server_start
        async def l3(app, loop):
            #print('L3')
            neighbor_monitor_thread = Thread(target=self.dc.monitor_neighbors)
            neighbor_monitor_thread.daemon = True
            neighbor_monitor_thread.start()
            #self.dc.monitor_neighbors()

        # Redirect to Sanic app run() function
        self.app.run(*args, **kwargs)
    
    def replace_chain(self, other: BlockChain):
        self.chain.replace(other)
        self.pending_transactions = []
        # TODO: Use to replace Miner L133 logic
    
    def make_transaction(self, transaction: Transaction):
        transaction_bytes = transaction.to_puzzle_bytes()

        if transaction_bytes in self.seen_transaction_hashes:
            # We can assume we have already processed this request
            #info(f'Already seen transaction {transaction}')
            return
        else:
            #info(f'Have not seen transaction {transaction}')
            self.seen_transaction_hashes.add(transaction_bytes)

        #info('A')
        if not transaction.is_valid():
            return
        
        #info('B')
        if self.miner.is_mining:
            # Add transaction to miner's current block
            self.miner.current_block.add_transaction(transaction)
            self.miner.current_block_changed = True
        else:
            self.pending_transactions.append(transaction)

        #info('C')
        self.dc.broadcast_transaction(transaction.to_json())
        #info('D')
    