from mimetypes import init
from threading import Thread
from typing import List
from sanic import Sanic
import inspect

from lc.comms import communication, discovery
from lc.blockchain import chain_manager

from sanic import Blueprint

#from lc.endpoints.node_bp import NodeBlueprint
from lc.endpoints import test_endpoints

import time

from lc.mining.miner import Miner


    
    #def bind(self, Node: node):



class Node:
    def __init__(self, pub_addr: str, initial_neighbors: List[str], mine: bool):
        self.app = Sanic("learncoin_full_node")
        self.pub_addr = pub_addr
        self.neighbors = initial_neighbors
        self.mine = mine

        self.app.blueprint(test_endpoints.bind(self))

        
    
    def start_mining(self):
        # Make sure server is running before we start mining
        while not self.app.is_running:
            time.sleep(1)
        miner = Miner(
            lambda: chain_manager.chain.blocks[-1] if chain_manager.chain.blocks else None,
            lambda block: chain_manager.chain.blocks.append(block),
            lambda: communication.broadcast_chain(chain_manager.chain)
        )
        miner.mine()
    
    def check_neighbors(self):
        while not self.app.is_running:
            time.sleep(1)
        discovery.test_neighbors()

    def run(self, *args, **kwargs):
        # !tmp
        for n in self.neighbors:
            discovery.add_neighbor(n)
        discovery.me = self.pub_addr
        if self.mine:
            mining_thread = Thread(target=self.start_mining)
            mining_thread.daemon = True
            mining_thread.start()
        discovery.discover_more_neighbors()
        neighbor_thread = Thread(target=self.check_neighbors)
        neighbor_thread.daemon = True
        neighbor_thread.start()

        # Redirect to Sanic app run() function
        self.app.run(*args, **kwargs)
    
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

