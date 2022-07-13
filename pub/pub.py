import zmq
import time
from datetime import datetime
import os

PUB_HOST = os.getenv('PUB_HOST', '127.0.0.1')
PUB_PORT = os.getenv('PUB_PORT', '5555')

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f'tcp://{PUB_HOST}:{PUB_PORT}')

poller = zmq.Poller()
poller.register(socket, zmq.POLLOUT)

print('starting publisher')

while True:
    socks = dict(poller.poll())

    if socket in socks:
        msg = {
            'id': 9999,
            'time': datetime.now()
        }

        print('sending msg')
        socket.send_pyobj(msg)
