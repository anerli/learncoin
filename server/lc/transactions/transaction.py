from lc.cryptography.primitives import PublicKey, PrivateKey, serialize_private_key, deserialize_public_key, secure_hash
from lc.util.conversions import float_from_bytes

from cryptography.exceptions import InvalidSignature

class Transaction:
    # Special constants for block reward transactions
    BLOCK_REWARD_SENDER = b'\0'*32
    BLOCK_REWARD_SIGNATURE = b'\0'*64

    def __init__(self, sender: bytes, receiver: bytes, amount: bytes, signature: bytes):
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
        return f'<Transaction sender={self.sender.hex()} receiver={self.receiver.hex()} amount={float_from_bytes(self.amount)} signature={self.signature.hex()}>'

    # def sender_hex(self):
    #     return self.sender.hex()
    def sender_key(self) -> PublicKey:
        return deserialize_public_key(self.sender)

    
    def is_valid(self) -> bool:
        '''
        Verifies that the given signature authenticates this transaction.
        Assumes that this is a standard transaction, not a block reward.
        '''

        # For easier consistency across Python / JS, we defined the combined byte value
        # of the transaction components as the concatenation of their hex values
        combined_hex = self.sender.hex() + self.receiver.hex() + self.amount.hex()
        print('Combined bytes as hex:', combined_hex)
        combined_bytes = bytes.fromhex(combined_hex)
        transaction_hash = secure_hash(combined_bytes)
        print('Hash as hex:', transaction_hash.hex())

        try:
            self.sender_key().verify(self.signature, transaction_hash)
            return True
        except InvalidSignature:
            return False
    
    def is_reward(self) -> bool:
        # Is this a block reward transaction?
        #print(self.sender)
        #print(self.sender == b'\0'*32)
        #print(self.signature == b'\0'*64)
        return self.sender == Transaction.BLOCK_REWARD_SENDER and self.signature == Transaction.BLOCK_REWARD_SIGNATURE

    def to_puzzle_bytes(self) -> bytes:
        '''
        Convert the data in this transaction to bytes that can be used
        in the computation of a block hash for a proof of work puzzle.
        '''
        return self.sender + self.receiver + self.amount + self.signature
    
    def to_json(self) -> dict:
        return dict(
            sender=self.sender.hex(),
            receiver=self.receiver.hex(),
            amount=self.amount.hex(),
            signature=self.signature.hex()
        )
    
    @classmethod
    def from_json(cls, data: dict) -> 'Transaction':
        return Transaction(
            sender=bytes.fromhex(data['sender']),
            receiver=bytes.fromhex(data['receiver']),
            amount=bytes.fromhex(data['amount']),
            signature=bytes.fromhex(data['signature']),
        )
