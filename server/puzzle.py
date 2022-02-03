DIFFICULTY = 4

def is_valid_proof(block_hash: bytes, proof: bytes):
    combined_bytes = block_hash + proof
    return combined_bytes.hex()[:DIFFICULTY] == "0"*DIFFICULTY