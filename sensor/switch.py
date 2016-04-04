import RPi.GPIO as GPIO

class Switch:
    status = False

    def __init__(self):
        self.status = False
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        

    def getStat(self):
        return self.status

    def checkStat(self):
        if GPIO.input(18) == False:
            print "switch on"
            if self.status == False:
                self.status = True

    def changeStat(self):
        self.status = False
	
