from sanic import Blueprint
import inspect

class NodeBlueprint(Blueprint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.routes = []

    def route(self, *args, **kwargs):
        # f: like a normal route function but can also take a Node first param, which will be this node
        '''
        e.g.
        @node.route('/chain')
        async def get_chain(node: Node, request):
            return node.chain.to_json()
        '''
        def wrapper_wrapper(f):
            if inspect.iscoroutinefunction(f):
                async def wrapper(*args, **kwargs):
                    return await f(self, *args, **kwargs)
            else:
                def wrapper(*args, **kwargs):
                    return f(self, *args, **kwargs)
            
            #self.app.add_route(wrapper, *args, **kwargs)
            self.routes.append((wrapper, args, kwargs))

        return wrapper_wrapper