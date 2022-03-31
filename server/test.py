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

from primitives import PrivateKey, serialize_private_key, deserialize_private_key, serialize_public_key

pkey = deserialize_private_key(bytes.fromhex('679df846fdf7118544654392e0b7a4b7473622581b28e1189793de5d694bce64'))
pubkey = pkey.public_key()
print(serialize_public_key(pubkey).hex())

# key = PrivateKey.generate()
# print(serialize_private_key(key).hex())

# print(serialize_public_key(key.public_key()).hex())