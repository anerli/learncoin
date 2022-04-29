import time
from numpy import False_
import requests
import threading

from lc.util import colors

def info(*args, error=False, **kwargs):
    color = colors.BLUE
    if error:
        color = colors.RED
    print(f'{color}<DISCOVERY🔎>{colors.RESET}', *args, **kwargs)

def err(*args, **kwargs):
    info(*args, **kwargs, error=True)

class DiscoveryComponent:
    def __init__(self, pub_addr, initial_neighbors):
        self.pub_addr = pub_addr
        self.neighbors = set(initial_neighbors)

        # For thread safety, lock for neighbors
        self.lock = threading.Lock()

    # https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery
    def discover_more_neighbors(self):
        if len(self.neighbors) == 0:
            return
        
        #print(self.neighbors)

        changes_made = True

        while changes_made:
            #print(self.neighbors)
            changes_made = False
            to_add = set()

            with self.lock:
                #print(self.neighbors)
                for n in self.neighbors:
                    #print('n:', n)
                    try:
                        resp = requests.get(f'http://{n}/discovery')
                        #print('received json:', resp.json())
                        addrs = resp.json()['neighbors']
                        info(f"Got neighbors {addrs} from {n}")
                        for addr in addrs:
                            #print('addr:', addr)
                            if addr not in self.neighbors and addr != self.pub_addr:
                                changes_made = True
                                to_add.add(addr)
                                #self.neighbors.add(addr)

                        data = self.json_neighbors()
                        _ = requests.post(f'http://{n}/discovery', json=data)
                    except requests.exceptions.ConnectionError:
                        err(f'Failed to connect to neighbor {n}')
                self.neighbors = self.neighbors.union(to_add)
                print(self.neighbors)

    def json_neighbors(self):
        #print('json:', {'neighbors': list(self.neighbors) + [self.pub_addr]})
        return {'neighbors': list(self.neighbors) + [self.pub_addr]}

    def monitor_neighbors(self):
        while True:
            #print(neighbors)
            time.sleep(60)
            #print('=== TESTING NEIGHBORS ===')
            with self.lock:
                for neighbor in self.neighbors:
                    try:
                        #print('Testing neighbor: ' + neighbor)
                        resp = requests.get('http://' + neighbor)
                        # Should get hello
                        if (resp.text == 'hello'):
                            continue
                        else:
                            self.neighbors.remove(neighbor)
                            #print('Invalid response: ' + resp.text)
                    except requests.exceptions.ConnectionError:
                        err(f'Failed to connect to neighbor {neighbor}, removing')
                        self.neighbors.remove(neighbor)
    
    def broadcast_chain(self, chain_data: dict):
        with self.lock:
            for neighbor in self.neighbors:
                url = 'http://' + neighbor + '/chain'
                info('BROADCASTING TO URL:', url)
                try:
                    resp = requests.post(url, json=chain_data)

                    if resp.status_code == 200:
                        info('Chain was accepted by neighbor.')
                    else:
                        info('Chain not accepted by neighbor; reason:', resp.text)
                except requests.exceptions.ConnectionError:
                    info('Could not broadcast chain to neighbor at:', url)