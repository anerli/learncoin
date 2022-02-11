from primitives import secure_hash

DIFFICULTY = 4

def is_valid_proof(block_hash: bytes, proof: bytes):
    # Do we even need to secure hash the block?
    # or do we just need the secure hash for the block bytes + proof?
    combined_bytes = block_hash + proof
    combined_hash = secure_hash(combined_bytes)
    #print(combined_hash.hex())#[:DIFFICULTY])
    return combined_hash.hex()[:DIFFICULTY] == "0"*DIFFICULTY