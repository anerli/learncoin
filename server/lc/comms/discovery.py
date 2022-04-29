# import requests
# from typing import List
# from sanic import Blueprint
# from sanic.response import text, json
# from lc.util import colors
# import time
# from requests.exceptions import ConnectionError

# def info(*args, error=False, **kwargs):
#     color = colors.BLUE
#     if error:
#         color = colors.RED
#     print(f'{color}<DISCOVERY🔎>{colors.RESET}', *args, **kwargs)

# def err(*args, **kwargs):
#     info(*args, **kwargs, error=True)

# # ===== Endpoints =====
# discovery_bp = Blueprint('discovery', url_prefix='/discovery')

# @discovery_bp.get("/")
# async def get_neighbors(request):
#     global neighbors
#     return json({'neighbors': neighbors + [me]})

# @discovery_bp.post("/")
# async def receive_neighbors(request):
#     global neighbors
#     addrs = request.json['neighbors']
#     if(len(addrs) < 0):
#         info("List was empty")
#         return text("list was empty", status=400)
#     for n in addrs:
#         if n not in neighbors and n != me:
#             add_neighbor(n)
#     msg = f"Received neighbors: {addrs}"
#     info(msg)
#     return text(msg, status=200)
# # ^^^^^ Endpoints ^^^^^



# # Each neighbor is a string of the format `ip:port`
# neighbors = []

# me = ''

# def add_neighbor(ip_port_str: str):
#     global neighbors
#     neighbors.append(ip_port_str)

# def get_neighbors() -> List[str]:
#     global neighbors
#     return neighbors

# # https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery
# def discover_more_neighbors():
#     global neighbors, me
#     if len(neighbors) != 0:
#         for n in neighbors:
#             try:
#                 resp = requests.get(f'http://{n}/discovery')
#                 addrs = resp.json()['neighbors']
#                 info(f"Got neighbors {addrs} from {n}")
#                 for addr in addrs:
#                     if addr not in neighbors and addr != me:
#                         neighbors.append(addr)

#                 data = {'neighbors': neighbors + [me]}
#                 _ = requests.post(f'http://{n}/discovery', json=data)
#             except ConnectionError:
#                 err(f'Failed to connect to neighbor {n}')


# # See https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery#Local_Client.27s_External_Address
# def get_my_external_ip():
#     pass

# def test_neighbors():
#     global neighbors
#     while True:
#         #print(neighbors)
#         time.sleep(60)
#         #print('=== TESTING NEIGHBORS ===')
#         for neighbor in neighbors:
#             try:
#                 #print('Testing neighbor: ' + neighbor)
#                 resp = requests.get('http://' + neighbor)
#                 # Should get hello
#                 if (resp.text == 'hello'):
#                     continue
#                 else:
#                     neighbors.remove(neighbor)
#                     #print('Invalid response: ' + resp.text)
#             except ConnectionError:
#                 neighbors.remove(neighbor)

#     # print('=== DONE TESTING NEIGHBORS ===')


