from lc.cryptography.primitives import PublicKey, PrivateKey, serialize_private_key, deserialize_public_key, secure_hash
from lc.util.conversions import float_from_bytes

from cryptography.exceptions import InvalidSignature

import math

class Transaction:
    # Special constants for block reward transactions
    BLOCK_REWARD_ID = b'\0'*16
    BLOCK_REWARD_SENDER = b'\0'*32
    BLOCK_REWARD_SIGNATURE = b'\0'*64
    BLOCK_REWARD_AMOUNT = 1.0

    def __init__(self, _id: bytes, sender: bytes, receiver: bytes, amount: bytes, signature: bytes):
        self.id = _id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
    
    # @classmethod
    # def block_reward(cls, receiver: bytes) -> 'Transaction':
    #     transaction = cls()
    #     transaction.sender = None
    #     tranaction.signature = 
    
    def __repr__(self):
        # print('amount: ', self.amount.hex())
        # print('amount float: ', float_from_bytes(self.amount))
        return f'<Transaction id={self.id.hex()} sender={self.sender.hex()} receiver={self.receiver.hex()} amount={float_from_bytes(self.amount)} signature={self.signature.hex()}>'

    # def sender_hex(self):
    #     return self.sender.hex()
    def sender_key(self) -> PublicKey:
        return deserialize_public_key(self.sender)

    
    def is_valid(self) -> bool:
        '''
        Verifies that the given signature authenticates this transaction.
        Assumes that this is a standard transaction, not a block reward.
        '''

        # If amount is invalid floating point number
        if math.isnan(float_from_bytes(self.amount)):
            return False
        
        if len(self.sender.hex()) != 64 or len(self.receiver.hex()) != 64:
            return False

        # For easier consistency across Python / JS, we defined the combined byte value
        # of the transaction components as the concatenation of their hex values
        combined_hex = self.id.hex() + self.sender.hex() + self.receiver.hex() + self.amount.hex()
        #print('Combined bytes as hex:', combined_hex)
        combined_bytes = bytes.fromhex(combined_hex)
        transaction_hash = secure_hash(combined_bytes)
        #print('Hash as hex:', transaction_hash.hex())

        try:
            self.sender_key().verify(self.signature, transaction_hash)
            return True
        except InvalidSignature:
            return False
    
    def is_valid_reward(self) -> bool:
        # Is this a block reward transaction?
        #print(self.sender)
        #print(self.sender == b'\0'*32)
        #print(self.signature == b'\0'*64)
        return self.id == Transaction.BLOCK_REWARD_ID and self.sender == Transaction.BLOCK_REWARD_SENDER and self.signature == Transaction.BLOCK_REWARD_SIGNATURE and float_from_bytes(self.amount) == Transaction.BLOCK_REWARD_AMOUNT

    def to_puzzle_bytes(self) -> bytes:
        '''
        Convert the data in this transaction to bytes that can be used
        in the computation of a block hash for a proof of work puzzle.
        '''
        return self.sender + self.receiver + self.amount + self.signature
    
    def to_json(self) -> dict:
        return dict(
            id=self.id.hex(),
            sender=self.sender.hex(),
            receiver=self.receiver.hex(),
            amount=self.amount.hex(),
            signature=self.signature.hex()
        )
    
    @classmethod
    def from_json(cls, data: dict) -> 'Transaction':
        return Transaction(
            _id=bytes.fromhex(data['id']),
            sender=bytes.fromhex(data['sender']),
            receiver=bytes.fromhex(data['receiver']),
            amount=bytes.fromhex(data['amount']),
            signature=bytes.fromhex(data['signature']),
        )
