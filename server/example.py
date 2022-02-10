from block import Block, BlockHeader
from chain import BlockChain, GENESIS_HASH
import puzzle

from time import time

# These conversions from https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3
def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
    
def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

# Reduce difficulty for testing purposes
puzzle.DIFFICULTY = 2

# Make new block without proof, no transactions
b = Block(BlockHeader(GENESIS_HASH))

# Try to prove block
proof = 0
start = time()
while True:
    print('Trying proof:', proof)
    #proof_bytes = 
    if puzzle.is_valid_proof(b.to_puzzle_hash(), int_to_bytes(proof)):
        break
    # Increment proof
    proof += 1
print(f'Proof found: {proof}')
print(f'Time to prove: {time() - start}')

# Add proof to block header
b.header.proof = int_to_bytes(proof)

print(f'Is block valid? {b.is_valid()}')


