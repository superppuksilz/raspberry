import sensor.light as light
import sensor.switch as switch
import subprocess

class FrontView:
    li = light.Light()
    swit = switch.Switch()
    cam = 0
    camStatus = 0

    def __init__(self):
        li = light.Light()
        swit = switch.Switch()
        cam = 0
        camStatus = 0

    def showView(self):
        self.swit.checkStat()
        self.li.setLight()
        bright = self.li.getLight()
        print bright

        if not self.swit.getStat():
            if (bright < 50 and self.camStatus == 0) :
                cmd = ["python", "/home/pi/asdf/raspberry/sensor/camera.py"]
                self.cam = subprocess.Popen(cmd, shell=False)
                self.camStatus = 1

        else:
            if self.camStatus == 1:
                self.cam.kill()
                self.camStatus = 0
                self.swit.changeStat()
        self.swit.changeStat()
        



		
