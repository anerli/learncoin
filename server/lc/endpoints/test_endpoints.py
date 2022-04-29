#from .node_bp import NodeBlueprint
from sanic.response import json, text
from typing import cast
from sanic import Blueprint

def bind(node):
    # Deferred import avoids circular dependencies
    from lc.node import Node
    from lc.cryptography.primitives import PrivateKey, deserialize_private_key, serialize_public_key, serialize_private_key

    node = cast(Node, node)

    bp = Blueprint('test')

    @bp.get("/")
    async def hello(request):
        return text("hello")

    @bp.get("/genkeypair")
    async def generate_private_key(request):
        # ! unsafe !
        # ! for easy key generation for testing !
        key = PrivateKey.generate()
        return json({'priv': serialize_private_key(key).hex(), 'pub': serialize_public_key(key.public_key()).hex()})

    @bp.post("/keycheck")
    async def check_valid_key(request):
        key = request.json['key']
        valid = True
        print(key)
        try:
            deserialize_private_key(bytes.fromhex(key))
        except ValueError:
            valid = False
        return json({'valid': valid})

    @bp.route("/node")
    async def test2(request):
        print(node)
        return text('ok')
    
    return bp