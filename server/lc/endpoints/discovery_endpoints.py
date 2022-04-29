from sanic import Blueprint
#from .node_bp import NodeBlueprint
from sanic.response import json, text
from lc.discovery import DiscoveryComponent
from lc.util import colors
from typing import cast

def info(*args, error=False, **kwargs):
    color = colors.BLUE
    if error:
        color = colors.RED
    print(f'{color}<DISCOVERY🔎>{colors.RESET}', *args, **kwargs)

def err(*args, **kwargs):
    info(*args, **kwargs, error=True)

def bind(dc):
    from lc.node import Node
    dc = cast(DiscoveryComponent, dc)

    discovery_bp = Blueprint('discovery', url_prefix='/discovery')

    @discovery_bp.get("/")
    async def get_neighbors(request):
        #global neighbors
        #return json({'neighbors': neighbors + [me]})
        return json(dc.json_neighbors())

    # @discovery_bp.post("/")
    # async def receive_neighbors(request):
    #     addrs = request.json['neighbors']
    #     if(len(addrs) < 0):
    #         info("List was empty")
    #         return text("list was empty", status=400)
    #     for n in addrs:
    #         if n not in dc.neighbors and n != dc.pub_addr:
    #             dc.neighbors.add(n)
    #     msg = f"Received neighbors: {addrs}"
    #     info(msg)
    #     return text(msg, status=200)
    
    return discovery_bp