class BlockHeader:
    def __init__(self, previous_block_hash: bytes, proof: bytes = None):
        self.previous_block_hash = previous_block_hash
        self.proof = proof
    
    def __repr__(self):
        return f"<BlockHeader previous_block_hash={self.previous_block_hash.hex()} proof={self.proof.hex() if self.proof else 'UNPROVEN'}>"

    def to_json(self) -> dict:
        return {
            'previous_block_hash': self.previous_block_hash.hex(),
            'proof': self.proof.hex() if self.proof else ''
        }
    #def to_dict(self) -> dict:
    @classmethod
    def from_json(cls, data: dict) -> 'BlockHeader':
        return BlockHeader(
            previous_block_hash=bytes.fromhex(data['previous_block_hash']),
            proof=bytes.fromhex(data['proof']) if data['proof'] != '' else None
        )
    
    def to_puzzle_bytes(self):
        '''
        Get the bytes of this header, to be used in the calculation
        of the proof of work puzzle.
        Excludes the proof since the puzzle hash is needed to find
        the proof in the first place.
        '''
        return self.previous_block_hash