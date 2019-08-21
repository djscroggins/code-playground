import asyncio
import functools
import time


def event_handler(loop, order_called, stop=False, delay=0):
    time.sleep(delay)
    print('Event handler {} called'.format(order_called))
    if stop:
        print('stopping the loop')
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    current_time = loop.time()
    try:
        print('Starting event loop ...')
        # This will get called even though it's delayed, because it is enqueued first
        loop.call_soon(functools.partial(event_handler, loop, 1, delay=15))
        loop.call_later(5, functools.partial(event_handler, loop, 2, delay=5))
        loop.call_later(1, functools.partial(event_handler, loop, 3))
        loop.call_soon(functools.partial(event_handler, loop, 4))
        # If set to just current_time, 2 and 3 will never be called, since higher, time-based execution priority
        loop.call_at(current_time + 10, functools.partial(event_handler, loop, 5, stop=True))
        loop.run_forever()
    finally:
        print('Closing event loop ...')
        loop.close()
