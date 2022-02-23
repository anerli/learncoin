import requests
from dataclasses import dataclass

@dataclass
class Neighbor:
    ip: str
    port: int
    # def __init__(self, ip: str, port: int):
    #     self.ip = ip
    #     self.port = port

# Localhost testing
# neighbors = [
#     '127.0.0.1', 
# ]

# Each neighbor is a string of the format `ip:port`
neighbors = []

def add_neighbor(ip_port_str: str):
    global neighbors
    ip = ip_port_str[:ip_port_str.find(':')]
    port = ip_port_str[ip_port_str.find(':')+1:]
    neighbors.append(Neighbor(ip, int(port)))

# https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery

# See https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery#Local_Client.27s_External_Address
def get_my_external_ip():
    pass

def test_neighbors():
    print('TESTING NEIGHBORS' + '!'*99)
    #resp = requests.get('https://google.com')#requests.get('http://127.0.0.1:8000')
    #resp = requests.get('http://127.0.0.1:8001')
    #print(resp)
    
    for neighbor in neighbors:
        resp = requests.get('http://' + neighbor.ip + ':' + str(neighbor.port))
        # Should get hello
        print(resp.text)
    print('DONE TESTING NEIGHBORS' + '!'*99)
