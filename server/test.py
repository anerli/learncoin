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

pkey = deserialize_private_key(bytes.fromhex('63abc05b43c21f8fd158ee24c1c7bd90fbce860358c44c0eb68859b098622181'))
pubkey = pkey.public_key()
print(serialize_public_key(pubkey).hex())

pubkey.verify(
    bytes.fromhex('0c030e9e40e7ac4dbc93a66469f5dfe073bb54d215a6944561aa77135a8f2ab2742d43ddb1d829c220e887ed6ee5cb57d20fd9210de136f6afe51322acf7a601'),
    bytes.fromhex('a762ae3cc8e23dfd451067573c4e6a43f6668c27924bba48ba305799c7a901ae')
)

# key = PrivateKey.generate()
# print(serialize_private_key(key).hex())

# print(serialize_public_key(key.public_key()).hex())