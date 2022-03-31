from primitives import PublicKey, PrivateKey, serialize_private_key, deserialize_public_key, secure_hash
from conversions import float_from_bytes
from sanic import Blueprint, Request
from sanic.response import json
from cryptography.exceptions import InvalidSignature
import colors

def info(*args, **kwargs):
    print(f'{colors.YELLOW}<TRANSACTIONS🪙>{colors.RESET}', *args, **kwargs)

# ▼▼▼▼▼ Transaction Endpoints ▼▼▼▼▼
transactions_bp = Blueprint('transactions', url_prefix='/transactions')

@transactions_bp.post('/')
def add_transaction(request: Request):
    # Sender public key
    sender = request.json['sender']
    # Receiver public key
    receiver = request.json['receiver']
    # Amount of LC as an IEEE 754 encoded float
    amount = request.json['amount']#float(request.json['amount'])
    # Signature
    signature = request.json['signature']

    sender_bytes = bytes.fromhex(sender)
    receiver_bytes = bytes.fromhex(receiver)
    amount_bytes = bytes.fromhex(amount)
    signature_bytes = bytes.fromhex(signature)

    # sender_key = deserialize_public_key(sender_bytes)
    # receiver_key = deserialize_public_key(receiver_key)

    transaction = Transaction(sender_bytes, receiver_bytes, amount_bytes, signature_bytes)
    info(f'Received transaction: {transaction}')

    print(f'Is valid? {transaction.is_valid()}')

    return json({'valid': transaction.is_valid()})
# ▲▲▲▲▲ Transaction Endpoints ▲▲▲▲▲


class Transaction:
    def __init__(self, sender: bytes, receiver: bytes, amount: bytes, signature: bytes):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
    
    def __repr__(self):
        return f'<Transaction sender={self.sender.hex()} receiver={self.receiver.hex()} amount={float_from_bytes(self.amount)} signature={self.signature.hex()}>'

    # def sender_hex(self):
    #     return self.sender.hex()
    def sender_key(self) -> PublicKey:
        return deserialize_public_key(self.sender)

    
    def is_valid(self) -> bool:
        '''
        Verifies that the given signature authenticates this transaction.
        '''

        # For easier consistency across Python / JS, we defined the combined byte value
        # of the transaction components as the concatenation of their hex values
        combined_hex = self.sender.hex() + self.receiver.hex()
        print('Combined bytes as hex:', combined_hex)
        combined_bytes = bytes.fromhex(combined_hex)
        transaction_hash = secure_hash(combined_bytes)
        print('Hash as hex:', transaction_hash.hex())

        
        '''
        # Concatenate transaction bytes
        transaction_bytes = self.sender + self.receiver# + self.amount
        print('Combined bytes as hex: ', transaction_bytes.hex())
        transaction_hash = secure_hash(transaction_bytes)
        print('Hash as hex: ', transaction_hash.hex())
        '''

        try:
            self.sender_key().verify(self.signature, transaction_hash)
            return True
        except InvalidSignature:
            return False
    

    def to_puzzle_bytes(self) -> bytes:
        '''
        Convert the data in this transaction to bytes that can be used
        in the computation of a block hash for a proof of work puzzle.
        '''
        return self.sender + self.receiver + self.amount + self.signature