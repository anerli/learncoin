from discovery import get_neighbors
from chain import BlockChain
import requests
import colors

def info(*args, **kwargs):
    print(f'{colors.CYAN}<COMMS>{colors.RESET}', *args, **kwargs)

def broadcast_chain(chain: BlockChain):
    neighbors = get_neighbors()

    for neighbor in neighbors:
        url = 'http://' + neighbor + '/chain'
        info('BROADCASTING TO URL:', url)
        try:
            resp = requests.post(url, json=chain.to_json())
        except requests.exceptions.ConnectionError:
            info('Could not broadcast chain to neighbor at:', url)
        if resp.status_code == 200:
            info('Chain was accepted by neighbor.')
        else:
            info('Chain not accepted by neighbor; reason:', resp.text)