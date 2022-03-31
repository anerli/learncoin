# from block import Block, BlockHeader
# from chain import BlockChain
# import json

# b = Block(BlockHeader(b'1234'))

# print(b)

# j = b.to_json()
# print(j)

# print(Block.from_json(j))

# chain = BlockChain([b, Block(BlockHeader(b'5678'))])

# print(chain)
# j = chain.to_json()

# print(j)
# print(BlockChain.from_json(j))

from primitives import PrivateKey, serialize_private_key, serialize_public_key

key = PrivateKey.generate()
print(serialize_private_key(key).hex())

print(serialize_public_key(key.public_key()).hex())