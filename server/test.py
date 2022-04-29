import time
import asyncio

import inspect

def mydec(*args, **kwargs):
    def wrapper_wrapper(f):
        print(args)
        if inspect.iscoroutinefunction(f):
            print('awaitable')
            async def wrapper(*args, **kwargs):
                await f('poop')
        else:
            print('not awaitable')
            def wrapper(*args, **kwargs):
                f('yarg')
        return wrapper
    return wrapper_wrapper

@mydec()
async def delay_print(msg):
    #print('hi')
    await asyncio.sleep(1)
    print('Delayed:', msg)

@mydec('potato')
def normal_print(msg):
    print('Normal:', msg)


async def main():
    await delay_print('hello')

normal_print('hi')
#delay_print('hello')

asyncio.run(main())

