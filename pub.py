import zmq
import time
from datetime import datetime

context = zmq.Context()

socket = context.socket(zmq.PUB)
PUB_HOST = '127.0.0.1'
PUB_PORT = '5555'
socket.bind(f'tcp://{PUB_HOST}:{PUB_PORT}')

print('starting publisher')

while True:
    msg = {
        'id': 9999,
        'time': datetime.now()
    }

    print('sending msg')
    socket.send_pyobj(msg)
    time.sleep(1)
