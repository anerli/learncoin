from sanic import Sanic
from sanic.response import json, text, file
from lc.blockchain.blockchain import BlockChain
from argparse import ArgumentParser
from lc.comms import discovery
from threading import Thread
from lc.comms import communication
from lc.transactions import transactions_endpoints
import time
from lc.mining.miner import Miner
#from chain_manager import chain
from lc.cryptography.primitives import PrivateKey, deserialize_private_key, serialize_private_key, serialize_public_key
from lc.blockchain import chain_manager

from lc.util.info import server_info as info

if __name__ == '__main__':
    argp = ArgumentParser()
    argp.add_argument('--mine', '-m', action='store_true', dest='mine')
    argp.add_argument('--port', '-p', dest='port', default=8000)
    argp.add_argument('--addr', '-a', dest='addr', default='localhost', help='IP or host where this node is publicly available.')
    argp.add_argument('--neighbors', '-n', dest='neighbors', nargs='+', metavar='<ip:port>',
        help='Initial neighbor nodes to use. An example of the format would be `127.0.0.1:8000`.')
    args = argp.parse_args()

    from lc.node import Node
    node = Node(
        pub_addr=f'{args.addr}:{args.port}',
        initial_neighbors=args.neighbors if args.neighbors else [],
        mine=args.mine
    )

    app = node.app

    # ===== Attach blueprints =====
    #app.blueprint(discovery.discovery_bp)
    app.blueprint(transactions_endpoints.transactions_bp)
    #app.blueprint(chain_manager.chain_bp)
    # ^^^^^ Attach blueprints ^^^^^

    node.run(host='0.0.0.0', debug=True, port=int(args.port))
    