from sanic import Blueprint, Request
from sanic.response import json, text

from lc.transactions.transaction import Transaction
from lc.util.conversions import float_from_bytes
from typing import cast


from lc.util.info import transactions_info as info


def bind(node):
    from lc.node import Node
    transactions_bp = Blueprint('transactions', url_prefix='/transactions')
    node = cast(Node, node)



    @transactions_bp.post('/')#, methods=['POST', 'OPTIONS'])
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

        valid = transaction.is_valid()
        info(f'Is valid? {valid}')

        #headers={"Access-Control-Allow-Origin": "*"}

        if not valid:
            return text('invalid transaction', status=400)

        # Check that user has enough to spend
        balance = node.chain.get_balance(transaction.sender.hex())

        print('Sender balance:', balance)

        if balance < float_from_bytes(transaction.amount):
            info('User does not have enough to perform provided transaction')
            return text('not enough LC to perform transaction', status=400) 

        node.make_transaction(transaction)

        return text('OK', status=200)
        #return json({'valid': valid})
    
    @transactions_bp.get('/balance/<pubkey>')
    async def get_balance(request, pubkey):
        # Get the total balance for the given hex public key address
        #return text('asd')
        # balances = node.chain.calculate_addr_totals()
        # if pubkey not in balances:
        #     balance = 0.0
        # else:
        #     balance = balances[pubkey]
        balance = node.chain.get_balance(pubkey)
        return json({'balance': balance})
    
    return transactions_bp
