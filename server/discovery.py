import requests
from typing import List

# Each neighbor is a string of the format `ip:port`
neighbors = []

def add_neighbor(ip_port_str: str):
    global neighbors
    neighbors.append(ip_port_str)

def get_neighbors() -> List[str]:
    global neighbors
    return neighbors
    

# https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery

# See https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery#Local_Client.27s_External_Address
def get_my_external_ip():
    pass

def test_neighbors():
    print('=== TESTING NEIGHBORS ===')
    for neighbor in neighbors:
        print('Testing neighbor: ' + neighbor)
        resp = requests.get('http://' + neighbor)
        # Should get hello
        if (resp.text == 'hello'):
            print('Test successful')
        else:
            print('Invalid response: ' + resp.text)
    print('=== DONE TESTING NEIGHBORS ===')
