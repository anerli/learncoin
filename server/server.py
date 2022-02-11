from sanic import Sanic
from sanic.response import json, text
from chain import BlockChain

app = Sanic("learncoin_full_node")

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

if __name__ == '__main__':
    chain = BlockChain()
    app.run()