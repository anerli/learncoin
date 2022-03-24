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
def get_addr():
    if(len(neighbors) != 0):
        for x in neighbors:
            try:
                resp = requests.get('http://'+ x+"/getaddr")
                addrs = resp.json()
                print(addrs)
                for addr in addrs['neighbors']:
                    print("gets in where I want")
                    if(addr not in neighbors):
                        neighbors.append(addr)
            except:
                print("adding neighbors went wrong")
            #try:
            #    data = {'neighbors': neighbors}
            #    print(requests.put('http://'+x+'/shareAddrs', data))
            #except:
            #    print("Posting neighbors went wrong")

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
