from discovery import get_neighbors
from chain import BlockChain
import requests

def broadcast_chain(chain: BlockChain):
    neighbors = get_neighbors()

    for neighbor in neighbors:
        requests.post('http://' + neighbor + '/chain', chain.to_json())
