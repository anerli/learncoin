from threading import Thread
from typing import List
from sanic import Sanic

from lc.comms import communication, discovery
from lc.blockchain import chain_manager

import time

from lc.mining.miner import Miner

class Node:
    def __init__(self, pub_addr: str, initial_neighbors: List[str], mine: bool):
        self.app = Sanic("learncoin_full_node")

        # !tmp
        for n in initial_neighbors:
            discovery.add_neighbor(n)
        discovery.me = pub_addr
        if mine:
            mining_thread = Thread(target=self.start_mining)
            mining_thread.daemon = True
            mining_thread.start()
        discovery.discover_more_neighbors()
        neighbor_thread = Thread(target=self.check_neighbors)
        neighbor_thread.daemon = True
        neighbor_thread.start()
    
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
        # Redirect to Sanic app run() function
        self.app.run(*args, **kwargs)

    def route(self, f):
        # f: like a normal route function but can also take a Node first param, which will be this node
        '''
        e.g.

        @node.route('/chain')
        async def get_chain(node: Node, request):
            return node.chain.to_json()
        '''
        #def wrapper()
        # TODO
        pass