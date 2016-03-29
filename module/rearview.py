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
        if(!swit.getStat()):
            ultra.setDist()
            dist = ultra.getDist()
            if(dist < 4):
                cam.showView(3)
        else:
            turnoffView()
	

    def turnoffView(self):
        
        return 


		
