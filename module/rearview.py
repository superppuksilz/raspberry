import sensor.ultrasonic as ultrasonic
import sensor.switch as switch
import subprocess

class RearView:
    ultra = ultrasonic.Ultrasonic()
    swit = switch.Switch()
    cam = 0
    camStatus = 0

    def __init__(self):
        ultra = ultrasonic.Ultrasonic()
        swit = switch.Switch()
        cam = 0
        camStatus = 0

    def showView(self):
        self.swit.checkStat()
        self.ultra.setDist()
        dist = self.ultra.getDist()
        print dist

        # if switch turns off, and distance less than 0.5 turn on the camera
        if not self.swit.getStat():
            if(dist < 0.5 and self.camStatus == 0):
                cmd = ["python", "/home/pi/asdf/raspberry/sensor/camera.py"]
                self.cam = subprocess.Popen(cmd, shell=False)
                self.camStatus = 1
        else:
            if self.camStatus == 1:
                self.cam.kill()
                self.camStatus = 0
                self.swit.changeStat()
        self.swit.changeStat()



		
