from sanic.response import json, text, file
from .blockchain import BlockChain
from sanic import Blueprint
#from lc.transactions import Transaction
from lc.util.conversions import float_from_bytes
from lc.comms.communication import broadcast_transaction
#from lc.mining.miner import is_mining, current_block
from lc.util.info import chain_info as info

from lc.transactions.transaction import Transaction

# Important shared object
chain = BlockChain()



# ▼▼▼▼▼ Chain Endpoints ▼▼▼▼▼
chain_bp = Blueprint('chain', url_prefix='/chain')

@chain_bp.post("/")
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
    info(f'Accepted chain of length {other_len}.')

    # PROBLEM: Chain object is referenced in other places
    #chain = other_chain
    chain.replace(other_chain)
    return text('Chain Accepted')

@chain_bp.get("/")
async def get_chain(request):
    return json(chain.to_json())
# ▲▲▲▲▲ Chain Endpoints ▲▲▲▲▲




    
