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
from chain_manager import chain

app = Sanic("learncoin_full_node")
#hain = BlockChain()

def info(*args, **kwargs):
    print('<SRV>', *args, **kwargs)

@app.get("/")
async def hello(request):
    return text("hello")

@app.get("/test")
async def test(request):
    discovery.test_neighbors()
    return text('aight')

@app.post("/chain")
async def receive_chain(request):
    # Endpoint for receiving chains, which have presumably mined a new block
    #print('=== RECEIVE CHAIN ===')
    # TODO: Separate this logic into another file (?)
    global chain
    #print(request.body)
    #print('Request JSON:', request.json)
    # ???? if request has no json this silently fails and freezes the call?? why???????
    other_chain = BlockChain.from_json(request.json)
    #print('What?')
    info('Received chain:', other_chain.describe())
    if not other_chain.is_valid():
        info('Received chain is invalid!')
        return text('invalid chain', status=400)
    if len(other_chain) <= len(chain):
        info(f'Chain received is not the longest (mine is {len(chain)}, theirs is {len(other_chain)}).')
        return text('i have a longer (or just as long) chain', status=418)
    # Replace chain
    info('Received longer valid chain, replacing own')
    chain = other_chain
    return text('Chain Accepted')


def start_mining():
    # Make sure server is running before we start mining
    while not app.is_running:
        time.sleep(1)
    
    mine()
    

if __name__ == '__main__':
    argp = ArgumentParser()
    argp.add_argument('--mine', action='store_true', dest='mine')
    argp.add_argument('--port', '-p', dest='port', default=8000)
    argp.add_argument('--neighbors', '-n', dest='neighbors', nargs='+', metavar='<ip:port>',
        help='Initial neighbor nodes to use. An example of the format would be `127.0.0.1:8000`.')
    args = argp.parse_args()

    if args.neighbors is not None:
        for n in args.neighbors:
            discovery.add_neighbor(n)

    print('Neighbors:', discovery.neighbors)

    if args.mine:
        mining_thread = Thread(target=start_mining)
        mining_thread.daemon = True
        mining_thread.start()
  
    app.run(debug=True, port=int(args.port))
