import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)
PUB_HOST = '127.0.0.1'
PUB_PORT = '5555'
socket.connect(f'tcp://{PUB_HOST}:{PUB_PORT}')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)
# socket.setsockopt(zmq.SUBSCRIBE, None)

print('starting receiver')

while True:
    socks = dict(poller.poll())

    if socket in socks:
        msg = socket.recv_pyobj()

        print(msg)


    
    # msg = socket.recv()

    # print(msg)
