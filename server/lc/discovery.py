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
        #self.lock = threading.Lock()

    # https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery
    def discover_more_neighbors(self):
        if len(self.neighbors) == 0:
            return
        
        #print(self.neighbors)

        changes_made = True

        # Copy this so any
        new_neighbors = self.neighbors.copy()

        while changes_made:
            #print(self.neighbors)
            changes_made = False
            to_add = set()

            #print('Acquiring lock 2')
            #with self.lock:
            #    print('Lock aquired 2')
                #print(self.neighbors)
            for n in new_neighbors:
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
            #self.neighbors = self.neighbors.union(to_add)
            #new_neighbors = new_neighbors.union(to_add)
            #print(self.neighbors)
            #print('Lock done 2')
        
        self.neighbors = new_neighbors

    def json_neighbors(self):
        #print('json:', {'neighbors': list(self.neighbors) + [self.pub_addr]})
        return {'neighbors': list(self.neighbors) + [self.pub_addr]}

    def monitor_neighbors(self):
        while True:
            #print(neighbors)
            time.sleep(60)
            #print('=== TESTING NEIGHBORS ===')
            #print('Acquiring lock 3')
            #with self.lock:
            #    print('Lock acquired 3')
            to_remove = set()
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
                    to_remove.add(neighbor)
                    #self.neighbors.remove(neighbor)
            
            # Copies neighbors implicitly so will not interfere with loops currently referencing self.neighbors
            self.neighbors -= to_remove
            #print('Lock done 3')
    def broadcast_chain(self, chain_data: dict):
        #print('Acquiring lock 1')
        #with self.lock:
        #    print('Lock acquired 1')
        for neighbor in self.neighbors:
            url = 'http://' + neighbor + '/chain'
            info('Broadcasting chain to:', url)
            try:
                resp = requests.post(url, json=chain_data)

                if resp.status_code == 200:
                    info('Chain was accepted by neighbor.')
                else:
                    info('Chain not accepted by neighbor; reason:', resp.text)
            except requests.exceptions.ConnectionError:
                info('Could not broadcast chain to neighbor at:', url)
         #   print('Lock done 1')
    def broadcast_transaction(self, transaction_data: dict):
        # We can make transactions as if we were a user to the other nodes
        #print('Acquiring lock')
        #with self.lock:
        #print('Lock acquired')
        for neighbor in self.neighbors:
            #print('Neighbor:', neighbor)
            url = 'http://' + neighbor + '/transactions'
            info('Forwarding transaction to:', url)
            try:
                #info('Posting')
                resp = requests.post(url, json=transaction_data)
                #info('Done posting')

                if resp.status_code == 200:
                    info('Transaction was accepted by neighbor.')
                else:
                    err('Transaction not accepted by neighbor; reason:', resp.text)
            except requests.exceptions.ConnectionError:
                info('Could not forward transaction to neighbor at:', url)
        #print('Done with lock')
        #print('Done broadcasting')