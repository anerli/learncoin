from argparse import ArgumentParser
from lc.node import Node

if __name__ == '__main__':
    argp = ArgumentParser()
    argp.add_argument('--mine', '-m', action='store_true', dest='mine')
    argp.add_argument('--port', '-p', dest='port', default=8000)
    argp.add_argument('--addr', '-a', dest='addr', default='localhost', help='IP or host where this node is publicly available.')
    argp.add_argument('--neighbors', '-n', dest='neighbors', nargs='+', metavar='<ip:port>',
        help='Initial neighbor nodes to use. An example of the format would be `127.0.0.1:8000`.')
    args = argp.parse_args()

    node = Node(
        pub_addr=f'{args.addr}:{args.port}',
        initial_neighbors=args.neighbors if args.neighbors else [],
        mine=args.mine
    )

    node.run(host='0.0.0.0', debug=True, port=int(args.port))
    