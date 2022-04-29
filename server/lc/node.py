from threading import Thread
from typing import List
from sanic import Sanic
import inspect
from lc.blockchain.blockchain import BlockChain

from lc.comms import communication, discovery
#from lc.blockchain import chain_manager

from sanic import Blueprint
from lc.discovery import DiscoveryComponent

#from lc.endpoints.node_bp import NodeBlueprint
from lc.endpoints import chain_endpoints, discovery_endpoints, test_endpoints, transactions_endpoints

import time

from lc.mining.miner import Miner
from lc.transactions.transaction import Transaction


    
    #def bind(self, Node: node):



class Node:
    def __init__(self, pub_addr: str, initial_neighbors: List[str], mine: bool):
        self.app = Sanic("learncoin_full_node")
        #self.pub_addr = pub_addr
        #self.neighbors = initial_neighbors
        self.mine = mine

        self.dc = DiscoveryComponent(pub_addr, initial_neighbors)

        self.chain = BlockChain()

        # Create miner whether or not we use it
        self.miner = Miner(
            lambda: self.chain.blocks[-1] if self.chain.blocks else None,
            lambda block: self.chain.blocks.append(block),
            lambda: self.dc.broadcast_chain(self.chain.to_json())
        )

        self.app.blueprint(test_endpoints.bind(self))
        self.app.blueprint(discovery_endpoints.bind(self.dc))
        self.app.blueprint(chain_endpoints.bind(self))
        self.app.blueprint(transactions_endpoints.bind(self))

        
    
    def start_mining(self):
        # Make sure server is running before we start mining
        while not self.app.is_running:
            time.sleep(1)
        
        self.miner.mine()
    
    def check_neighbors(self):
        while not self.app.is_running:
            time.sleep(1)
        self.dc.update_neighbors()

    def run(self, *args, **kwargs):
        if self.mine:
            mining_thread = Thread(target=self.start_mining)
            mining_thread.daemon = True
            mining_thread.start()
        #discovery.discover_more_neighbors()
        self.dc.discover_more_neighbors()

        # neighbor_thread = Thread(target=self.check_neighbors)
        # neighbor_thread.daemon = True
        # neighbor_thread.start()

        # Redirect to Sanic app run() function
        self.app.run(*args, **kwargs)
    
    def make_transaction(self, transaction: Transaction):
        if self.miner.is_mining:
            # Add transaction to miner's current block
            self.miner.current_block.add_transaction(transaction)
            self.miner.current_block_changed = True


        # TODO: Broadcast transaction
        pass
    
    #def blueprint(self, bp: Blueprint):
    #    self.app.blueprint(bp)
        # for route in bp.routes:
        #     wrapper = route[0]
        #     args = route[1]
        #     kwargs = route[2]
        #     self.app.add_route(wrapper, *args, **kwargs)

    # def route(self, *args, **kwargs):
    #     # f: like a normal route function but can also take a Node first param, which will be this node
    #     '''
    #     e.g.
    #     @node.route('/chain')
    #     async def get_chain(node: Node, request):
    #         return node.chain.to_json()
    #     '''
    #     def wrapper_wrapper(f):
    #         if inspect.iscoroutinefunction(f):
    #             async def wrapper(*args, **kwargs):
    #                 return await f(self, *args, **kwargs)
    #         else:
    #             def wrapper(*args, **kwargs):
    #                 return f(self, *args, **kwargs)
            
    #         self.app.add_route(wrapper, *args, **kwargs)

    #     return wrapper_wrapper

