
import picamera
import time

class Camera:
    camera = 0

    def __init__(self):
        camera = 0

    def showView(self, t):
        with picamera.PiCamera() as camera:
	    camera.start_preview()
	    time.sleep(t)
	    camera.stop_preview()

    def turnoffView():
        a = 1

    def caputurePic(self):
        a=1
        #need to fill

		
