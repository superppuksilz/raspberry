import sensor.camera as camera
import sensor.ultrasonic as ultrasonic
import sensor.switch as switch

class RearView:
    ultra = ultrasonic.Ultrasonic()
    cam = camera.Camera()
    swit = switch.Switch()

    def __init__(self):
        ultra = ultrasonic.Ultrasonic()
        cam = camera.Camera()
        swit = switch.Switch()

    def showView(self):
        self.swit.checkStat()
        if not self.swit.getStat():
            self.ultra.setDist()
            dist = self.ultra.getDist()
            print dist
            if(dist < 0.5):
                self.cam.showView()
        else:
            self.turnoffView()
	

    def turnoffView(self):
        self.cam.turnoffView()
        self.swit.changeStat()


		
