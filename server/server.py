from sanic import Sanic
from sanic.response import json, text
from chain import BlockChain
from argparse import ArgumentParser

app = Sanic("learncoin_full_node")

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

if __name__ == '__main__':
    argp = ArgumentParser()
    argp.add_argument('--mine', action='store_true')
    argp.add_argument('--')

    chain = BlockChain()
    app.run()