from transaction import Transaction
from typing import List
from primitives import secure_hash
from puzzle import is_valid_proof

class BlockHeader:
    def __init__(self, previous_block_hash: bytes, proof: bytes = None):
        self.previous_block_hash = previous_block_hash
        self.proof = proof
    
    def __repr__(self):
        return f'<BlockHeader previous_block_hash={self.previous_block_hash.hex()} proof={self.proof.hex()}>'

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
        self.header = header
        self.transactions = transactions
    
    def __repr__(self):
        return f'<Block header={self.header} transactions={self.transactions}>'
    
    def to_json(self) -> dict:
        '''
        Serializes block data to a dictionary which can be passed as json
        to other servers.
        '''
        # TODO
        pass
    
    def to_puzzle_bytes(self) -> bytes:
        byte_sum = b'\x00' # 0 as bytes
        byte_sum += self.header.to_puzzle_bytes()

        for transaction in self.transactions:
            byte_sum += transaction.to_puzzle_bytes()
        
        return byte_sum
    
    def to_puzzle_hash(self) -> bytes:
        return secure_hash(self.to_puzzle_bytes())
    
    # def is_proven(self) -> bool:
    #     '''
    #     Returns true if this block contains a proof and false otherwise.
    #     Does NOT check whether the proof is actually valid or not.
    #     '''
    #     return self.header.proof is not None
    
    def is_valid(self) -> bool:
        '''
        Returns true if this block is proven, has a valid proof, 
        and has all valid transactions.
        '''
        
        # === Verify proof ===
        # Check if there is even a proof contained in the header
        #if not self.is_proven():
        if self.header.proof is None:
            return False
        # Do actual verification of proof
        if not is_valid_proof(self.to_puzzle_hash(), self.header.proof):
            return False
        
        # === Verify transaction signatures ===
        # TODO

        # === Verify address sums ===
        # TODO

        # Everything is valid if we get here
        return True
