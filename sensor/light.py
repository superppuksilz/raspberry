import RPi.GPIO as gpio


class Light:
    value = 0.1

    def __init__(self):
        value = 0.1
        gpio.setmode(gpio.BCM)
        gpio.setup(4, gpio.IN)
        
    def setBright(self):
        print gpio.input(4)
        
    def getBright(self):
        return value
		
