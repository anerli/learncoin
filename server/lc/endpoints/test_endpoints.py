from .node_bp import NodeBlueprint
from sanic.response import json, text

def build():
    # Deferred import avoids circular dependencies
    from lc.node import Node
    from lc.cryptography.primitives import PrivateKey, deserialize_private_key, serialize_public_key, serialize_private_key
    from lc.comms import discovery

    bp = NodeBlueprint('test')

    @bp.get("/")
    async def hello(node: Node, request):
        return text("hello")

    @bp.get("/test")
    async def test(node: Node, request):
        discovery.test_neighbors()
        return text('aight')

    @bp.get("/genkeypair")
    async def generate_private_key(node: Node, request):
        # ! unsafe !
        # ! for easy key generation for testing !
        key = PrivateKey.generate()
        return json({'priv': serialize_private_key(key).hex(), 'pub': serialize_public_key(key.public_key()).hex()})

    @bp.post("/keycheck")
    async def check_valid_key(node: Node, request):
        key = request.json['key']
        valid = True
        print(key)
        try:
            deserialize_private_key(bytes.fromhex(key))
        except ValueError:
            valid = False
        return json({'valid': valid})


    @bp.route("/node")
    async def test2(node: Node, request):
        print(node)
        return text('ok')
    
    return bp