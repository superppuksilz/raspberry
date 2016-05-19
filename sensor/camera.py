
import picamera
import time

with picamera.PiCamera() as camera:
    #camera.resoultion = (320, 240)
    camera.start_preview(fullscreen = True, window=(50, 50, 320, 240))
    time.sleep(1000)
