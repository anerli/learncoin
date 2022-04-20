from sanic import Sanic
from sanic.response import json, text, file
from lc.blockchain import BlockChain
from argparse import ArgumentParser
from lc.comms import discovery
from threading import Thread
from lc.comms import communication
from lc import transactions
import time
from lc.mining.miner import mine
#from chain_manager import chain
from lc.cryptography.primitives import PrivateKey, deserialize_private_key, serialize_private_key, serialize_public_key
from lc.blockchain import chain_manager

from lc.util.info import server_info as info

app = Sanic("learncoin_full_node")


# ===== Attach blueprints =====
app.blueprint(discovery.discovery_bp)
app.blueprint(transactions.transactions_bp)
app.blueprint(chain_manager.chain_bp)
# ^^^^^ Attach blueprints ^^^^^


@app.get("/")
async def hello(request):
    return text("hello")

@app.get("/test")
async def test(request):
    discovery.test_neighbors()
    return text('aight')


# @app.get("/genprivkey")
# async def generate_private_key(request):
#     # ! unsafe !
#     key = PrivateKey.generate()
#     return json({'key': serialize_private_key(key).hex()})

@app.get("/genkeypair")
async def generate_private_key(request):
    # ! unsafe !
    # ! for easy key generation for testing !
    key = PrivateKey.generate()
    return json({'priv': serialize_private_key(key).hex(), 'pub': serialize_public_key(key.public_key()).hex()})

@app.post("/keycheck")
async def check_valid_key(request):
    key = request.json['key']
    valid = True
    print(key)
    try:
        deserialize_private_key(bytes.fromhex(key))
    except ValueError:
        valid = False
    return json({'valid': valid})


def start_mining(chain):
    # Make sure server is running before we start mining
    while not app.is_running:
        time.sleep(1)
    mine(chain)

if __name__ == '__main__':
    argp = ArgumentParser()
    argp.add_argument('--mine', '-m', action='store_true', dest='mine')
    argp.add_argument('--port', '-p', dest='port', default=8000)
    argp.add_argument('--neighbors', '-n', dest='neighbors', nargs='+', metavar='<ip:port>',
        help='Initial neighbor nodes to use. An example of the format would be `127.0.0.1:8000`.')
    args = argp.parse_args()

    if args.neighbors is not None:
        for n in args.neighbors:
            discovery.add_neighbor(n)
    
    # ! tmp
    discovery.me = f'localhost:{args.port}'

    print('Neighbors:', discovery.neighbors)

    if args.mine:
        mining_thread = Thread(target=start_mining, args=[chain_manager.chain])
        mining_thread.daemon = True
        mining_thread.start()

    discovery.discover_more_neighbors()

    app.run(host='0.0.0.0', debug=True, port=int(args.port))



