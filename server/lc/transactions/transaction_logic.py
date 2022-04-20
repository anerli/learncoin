# from .transaction import Transaction
# import lc.blockchain.chain_manager
# from lc.mining.miner import is_mining, current_block

# def make_transaction(transaction: Transaction):
#     '''
#     Make a transaction by adding it to the latest block and notifying neighbors of it.
#     Called by transaction endpoint as well as miner when a block is mined.
#     '''
#     global chain
#     info(f'Making transaction:')
#     print(f'\tsender: {transaction.sender.hex()}')
#     print(f'\treceiver: {transaction.receiver.hex()}')
#     print(f'\tamount: {float_from_bytes(transaction.amount)}')
#     print(f'\tsignature: {transaction.signature.hex()}')
#     info(f'Is valid? {transaction.is_valid()}')
