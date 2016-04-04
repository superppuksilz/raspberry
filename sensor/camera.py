
import picamera
import time

class Camera:
    camera = 0

    def __init__(self):
        camera = 0

    def showView(self):
        with picamera.PiCamera() as camera:
	    camera.start_preview()
	    
    def turnoffView(self):
        with picamera.PiCamera() as camera:
            camera.stop_preview()

    def caputurePic(self):
        a=1
        #need to fill

		
