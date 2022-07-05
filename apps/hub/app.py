# run this program on the Mac to display image streams from multiple RPis
import cv2
import imagezmq
import datetime

def processImage(image):
    # timestamp = datetime.datetime.now()
    # ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    # cv2.putText(image, ts, (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
    # 0.35, (0, 0, 255), 1)
    # Do something useful here, for example, run motion detection and record
    # a stream to a file if detected.
    pass

# Create a hub for receiving images from cameras
image_hub = imagezmq.ImageHub()

# Create a PUB server to send images for monitoring purposes in a non-blocking mode
stream_monitor = imagezmq.ImageSender(connect_to = 'tcp://*:5566', REQ_REP = False)

# Start main loop
while True:
    rpi_name, image = image_hub.recv_image()
    image_hub.send_reply(b'OK')
    processImage(image)
    stream_monitor.send_image(rpi_name, image)
