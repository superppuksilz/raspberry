
import picamera
import time

class Camera:
    camera = 0

    def __init__(self):
        camera = picamera.PiCamera()

    def showView(self, t):
	    camera.start_preview()
	    time.sleep(t)
	    camera.stop_preview()

    def turnoffView():
        

    def caputurePic(self):
        #need to fill

		
