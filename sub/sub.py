import zmq
import time
import os


PUB_HOST = os.getenv('PUB_HOST', '127.0.0.1')
PUB_PORT = os.getenv('PUB_PORT', '5555')

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f'tcp://{PUB_HOST}:{PUB_PORT}')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)

print('starting receiver')

while True:
    socks = dict(poller.poll())

    if socket in socks:
        msg = socket.recv_pyobj()

        print(msg)
