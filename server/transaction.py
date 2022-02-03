from primitives import PrivateKey

class Transaction:
    
    def to_puzzle_bytes(self) -> bytes:
        '''
        Convert the data in this transaction to bytes that can be used
        in the computation of a block hash for a proof of work puzzle.
        '''
        # TODO
        pass