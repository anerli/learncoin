from venv import create
from lc import transactions
from lc.util import colors

def create_info_function(color, prefix: str):
    def info_func(*args, **kwargs):
        print(f'{color}<{prefix}>{colors.RESET}', *args, **kwargs)
    return info_func

# def transactions_info(*args, **kwargs):
#     print(f'{colors.YELLOW}<TRANSACTIONS🪙>{colors.RESET}', *args, **kwargs)

# def comms_info(*args, **kwargs):
#     print(f'{colors.CYAN}<COMMS📶>{colors.RESET}', *args, **kwargs)


transactions_info = create_info_function(colors.YELLOW, 'TRANSACTIONS🪙')
comms_info = create_info_function(colors.CYAN, 'COMMS📶')
mining_info = create_info_function(colors.YELLOW, 'MINING⛏')
chain_info = create_info_function(colors.MAGENTA, 'CHAIN⛓')
server_info = create_info_function(colors.MAGENTA, 'SRV🖳')
