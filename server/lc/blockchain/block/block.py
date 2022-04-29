from lc.transactions.transaction import Transaction
from typing import List
from lc.cryptography.primitives import secure_hash
from lc.cryptography.puzzle import is_valid_proof
from lc.util.conversions import float_from_bytes
from .block_header import BlockHeader



class Block:
    def __init__(self, header: BlockHeader, transactions: List[Transaction] = None):
        if transactions is None:
            transactions = []
        self.header = header
        self.transactions = transactions
    
    def __repr__(self):
        return f'<Block header={self.header} transactions={self.transactions}>'
    
    def to_json(self) -> dict:
        '''
        Serializes block data to a dictionary which can be passed as json
        to other servers.
        '''
        return {
            'header': self.header.to_json(),
            'transactions': [transaction.to_json() for transaction in self.transactions]
        }
    
    @classmethod
    def from_json(cls, data: dict) -> 'Block':
        return Block(
            header=BlockHeader.from_json(data['header']),
            transactions=[Transaction.from_json(j) for j in data['transactions']]
        )
    
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

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
    
    def is_valid(self) -> bool:
        '''
        Returns true if this block is proven, has a valid proof, 
        and has all valid transactions.
        '''
        
        # === Verify proof ===
        # Check if there is even a proof contained in the header
        #if not self.is_proven():
        if self.header.proof is None:
            print('Invalid block: No proof')
            return False
        # Do actual verification of proof
        if not is_valid_proof(self.to_puzzle_hash(), self.header.proof):#!
            print('Invalid block: Invalid proof: ' + self.header.proof.hex())
            return False
        

        # TODO: Account for block reward
        seen_block_reward = False
        # === Verify transaction signatures ===
        for transaction in self.transactions:
            # Can have at most one block reward
            if not seen_block_reward and transaction.is_valid_reward():
                seen_block_reward = True
                continue
            if not transaction.is_valid():
                print('Invalid block: Invalid transaction:', transaction)
                return False

        # === Verify address sums ===
        balances = self.calculate_addr_totals()
        for k, v in balances:
            if v < 0.0:
                print(f'Invalid block: Negative balance {v} for addr {k}.')
                return False

        # Everything is valid if we get here
        return True
    
    def calculate_addr_totals(self) -> dict:
        # Calculate the total balance of each public key address according to the transactions
        # in this block
        totals = {}
        for transaction in self.transactions:
            # Reward or normal block, add to receiver's balance
            receiver = transaction.receiver.hex()

            if receiver in totals:
                totals[receiver] += float_from_bytes(transaction.amount)
            else:
                totals[receiver] = float_from_bytes(transaction.amount)
            
            if not transaction.is_valid_reward():
                # Non-Reward block, so make sure to subtract from sender's balance as well
                sender = transaction.sender.hex()

                if sender in totals:
                    totals[sender] -= float_from_bytes(transaction.amount)
                else:
                    totals[sender] = float_from_bytes(transaction.amount)

        return totals
