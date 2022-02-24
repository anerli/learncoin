from discovery import get_neighbors
from chain import BlockChain
import requests

def broadcast_chain(chain: BlockChain):
    neighbors = get_neighbors()

    for neighbor in neighbors:
        url = 'http://' + neighbor + '/chain'
        print('BROADCASTING TO URL:', url)
        try:
            requests.post(url, json=chain.to_json())
        except requests.exceptions.ConnectionError:
            print('Could not broadcast chain to neighbor at:', url)
