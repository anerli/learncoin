from dis import disco
from sanic import Sanic
from sanic.response import json, text
from chain import BlockChain
from argparse import ArgumentParser
import discovery
from threading import Thread
import communication
import time
from mining import mine
#from chain_manager import chain
import colors
import json

app = Sanic("learncoin_full_node")
chain = BlockChain()

def info(*args, **kwargs):
    print(f'{colors.MAGENTA}<SRV🖳>{colors.RESET}', *args, **kwargs)

@app.get("/")
async def hello(request):
    return text("hello")

@app.get("/test")
async def test(request):
    discovery.test_neighbors()
    return text('aight')

@app.route("/getaddr")
async def get_addr(request):
    with open('server/addresses.json', 'r') as f:
        data = json.load(f)
    return text(json.dumps(data))

@app.post("/chain")
async def receive_chain(request):
    # Endpoint for receiving chains, which have presumably mined a new block
    #print('=== RECEIVE CHAIN ===')
    # TODO: Separate this logic into another file (?)
    global chain
    # ? if request has no json this silently fails and freezes the call? why?
    other_chain = BlockChain.from_json(request.json)
    if not other_chain.is_valid():
        info('Received chain is invalid!')
        return text('Received chain is invalid.', status=400)
    other_len = len(other_chain)
    my_len = len(chain)
    if other_len <= my_len:
        # FIXME Future Problem: if chains are same length but carry different transactions and proofs then each chain will
        # be valid but have different blocks at certain points.
        # One way to fix would be finding a way to merge the chains and have both nodes agree on that one.
        msg = f'Received chain of length {other_len} is not longer than local chain of length {my_len}.'
        info(msg)
        return text(msg, status=400)
    # Replace chain
    #info('Received longer valid chain, replacing own')
    info(f'Accepted chain of length {other_len}.')

    # PROBLEM: Chain object is referenced in other places
    #chain = other_chain
    chain.replace(other_chain)
    return text('Chain Accepted')

@app.get("/chain")
async def get_chain(request):
    return json(chain.to_json())

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

    print('Neighbors:', discovery.neighbors)

    if args.mine:
        mining_thread = Thread(target=start_mining, args=[chain])
        mining_thread.daemon = True
        mining_thread.start()
  
    app.run(debug=True, port=int(args.port))


