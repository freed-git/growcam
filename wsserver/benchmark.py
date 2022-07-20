#!/usr/bin/env python

import asyncio
from socket import timeout
import sys
import websockets
import time


URI = "ws://localhost:32080"


async def run(client_id, messages):
    # t0 = time.perf_counter()
    try:
        async with websockets.connect(URI, timeout=60) as websocket:
            for message_id in range(messages):
                await websocket.send("{client_id}:{message_id}")
                await websocket.recv()
    except Exception as e:
        print(e)
        # t1 = time.perf_counter()
        # print(f"Connection latency: {t1 - t0} seconds")
        # sys.stdout.flush()
        # sys.stderr.flush()


async def benchmark(clients, messages):
    await asyncio.wait([
        asyncio.create_task(run(client_id, messages)) for client_id in range(clients)
    ])


if __name__ == "__main__":
    # clients, messages = int(sys.argv[1]), int(sys.argv[2])
    t0 = time.perf_counter()
    clients = 500
    messages = 6
    # if sys.platform == 'win32':
    #     loop = asyncio.ProactorEventLoop()
    #     asyncio.set_event_loop(loop)
    try:
        asyncio.run(benchmark(clients, messages))
    except Exception as e:
        print(e)
        # for task in asyncio.Task.all_tasks():
        #     task.cancel()
        # exit(1)
    t1 = time.perf_counter()
    print(f"Connection latency: {t1 - t0} seconds")
    sys.stdout.flush()
    sys.stderr.flush()


# ping_interval
# ping_timeout
