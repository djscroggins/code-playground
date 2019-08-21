import asyncio
import functools
import time


def event_handler(loop, stop=False, delay=0):
    time.sleep(delay)
    print('Event handler called')
    if stop:
        print('stopping the loop')
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        # call_soon is FIFO
        loop.call_soon(functools.partial(event_handler, loop, delay=5))
        print('starting event loop')
        loop.call_soon(functools.partial(event_handler, loop, stop=True))
        loop.run_forever()
    finally:
        print('closing event loop')
        loop.close()
