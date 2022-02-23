from dis import disco
from sanic import Sanic
from sanic.response import json, text
from chain import BlockChain
from argparse import ArgumentParser
import discovery
from threading import Thread
import communication

app = Sanic("learncoin_full_node")

@app.get("/")
async def hello(request):
    return text("hello")

@app.get("/test")
async def test(request):
    discovery.test_neighbors()
    print('HERE' + '&'*99)
    return text('aight')

if __name__ == '__main__':
    argp = ArgumentParser()
    argp.add_argument('--mine', action='store_true', dest='mine')
    argp.add_argument('--port', '-p', dest='port', default=8000)
    argp.add_argument('--neighbors', '-n', dest='neighbors', nargs='+', metavar='<ip:port>',
        help='Initial neighbor nodes to use. An example of the format would be `127.0.0.1:8000`.')
    args = argp.parse_args()

    #print(args.port)
    print(args.neighbors)
    #discovery.neighbors = args.neighbors
    if args.neighbors is not None:
        for n in args.neighbors:
            discovery.add_neighbor(n)

    print('Neighbors:', discovery.neighbors)

    
    #server_thread = Thread(target=app.run)
    #server_thread.daemon = True

    # communication_thread = Thread(target=communication.start)
    # communication_thread.daemon = True

    chain = BlockChain()
    #server_thread.start()
    # communication_thread.start()    
    app.run(debug=True, port=int(args.port))

    # print('App is running')

    # import time
    # time.sleep(10)

    # discovery.test_neighbors()