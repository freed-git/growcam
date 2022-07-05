import socket
import time
from imutils.video import VideoStream, FPS
import imagezmq
import zmq
import traceback
import cv2
# import datetime

def create_sender(connect_to=None):
    sender = imagezmq.ImageSender(connect_to=connect_to)
    sender.zmq_socket.setsockopt(zmq.LINGER, 0)
    sender.zmq_socket.setsockopt(zmq.RCVTIMEO, 2000)
    sender.zmq_socket.setsockopt(zmq.SNDTIMEO, 2000)
    return sender

connect_to='tcp://192.168.1.201:5555'
sender = create_sender(connect_to=connect_to)
time_between_restarts = 5

rpi_name = socket.gethostname() # send unique RPi hostname with each image
picam = VideoStream(usePiCamera=True, resolution=(240, 180)).start()
time.sleep(2.0)  # allow camera sensor to warm up

fps = FPS().start()

while True:  # send images as stream until Ctrl-C
    image = picam.read()

    fps.update()
    fps.stop()

    result = str(fps.fps())

    # timestamp = datetime.datetime.now()
    # ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(image, result, (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
    0.35, (0, 0, 255), 1)

    try:
        sender.send_image(rpi_name, image)
    except Exception as e:
        print('Python error with no Exception handler:')
        print('Traceback error:', e)
        traceback.print_exc()
        if 'sender' in locals():
            print('Closing ImageSender.')
            sender.close()
        time.sleep(time_between_restarts)
        print('Restarting ImageSender.')
        sender = create_sender(connect_to=connect_to)
