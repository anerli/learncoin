from lc.comms.discovery import get_neighbors
from lc.blockchain import BlockChain
import requests
#import colors
from lc.util.info import comms_info as info


def broadcast_chain(chain: BlockChain):
    neighbors = get_neighbors()

    for neighbor in neighbors:
        url = 'http://' + neighbor + '/chain'
        info('BROADCASTING TO URL:', url)
        try:
            resp = requests.post(url, json=chain.to_json())

            if resp.status_code == 200:
                info('Chain was accepted by neighbor.')
            else:
                info('Chain not accepted by neighbor; reason:', resp.text)
        except requests.exceptions.ConnectionError:
            info('Could not broadcast chain to neighbor at:', url)
        