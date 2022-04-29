from sanic import Blueprint, Request
from sanic.response import json

from lc.transactions.transaction import Transaction
from lc.util.conversions import float_from_bytes
from typing import cast


from lc.util.info import transactions_info as info


def bind(node):
    from lc.node import Node
    transactions_bp = Blueprint('transactions', url_prefix='/transactions')
    node = cast(Node, node)

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
        info(f'Received transaction:')
        print(f'\tsender: {transaction.sender.hex()}')
        print(f'\treceiver: {transaction.receiver.hex()}')
        print(f'\tamount: {transaction.amount.hex()} -> {float_from_bytes(transaction.amount)}')
        print(f'\tsignature: {transaction.signature.hex()}')

        info(f'Is valid? {transaction.is_valid()}')

        # ?
        #chain_manager.make_transaction(transaction)
        # !FIXME
        #make_transaction(transaction)

        return json({'valid': transaction.is_valid()})
    
    return transactions_bp
