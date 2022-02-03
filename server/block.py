from transaction import Transaction
from typing import List
from primitives import secure_hash
from puzzle import is_valid_proof

class BlockHeader:
    def __init__(self, previous_block_hash: bytes, proof: bytes = None):
        self.previous_block_hash = previous_block_hash
        self.proof = proof

    def to_puzzle_bytes(self):
        '''
        Get the bytes of this header, to be used in the calculation
        of the proof of work puzzle.
        Excludes the proof since the puzzle hash is needed to find
        the proof in the first place.
        '''
        return self.previous_block_hash

class Block:
    def __init__(self, header: BlockHeader, transactions: List[Transaction] = []):
        self.transactions = transactions
        self.header = header
    
    def to_json(self) -> dict:
        '''
        Serializes block data to a dictionary which can be passed as json
        to other servers.
        '''
        # TODO
        pass
    
    def to_puzzle_bytes(self) -> bytes:
        byte_sum = 0
        byte_sum += self.header.to_puzzle_bytes()

        for transaction in self.transactions:
            byte_sum += transaction.to_puzzle_bytes()
        
        return byte_sum
    
    def to_puzzle_hash(self) -> bytes:
        return secure_hash(self.to_puzzle_bytes())
    
    def is_proven(self) -> bool:
        '''
        Returns true if this block contains a proof and false otherwise.
        Does NOT check whether the proof is actually valid or not.
        '''
        return self.header.proof is not None
    
    def is_valid(self) -> bool:
        '''
        Returns true if this block is proven, has a valid proof, 
        and has all valid transactions.
        '''
        
        # === Verify proof ===
        if not self.is_proven():
            return False
        # TODO: Do actual verification
        
        # === Verify transaction signatures ===
        # TODO

        # === Verify address sums ===
        # TODO
