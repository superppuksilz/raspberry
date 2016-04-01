import RPi.GPIO as gpio
import picamera
import time


gpio.setmode(gpio.BCM)

trig = 13
echo = 19

print "start"

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

try:
	while True:
		gpio.output(trig, False)
		time.sleep(0.5)
		
		gpio.output(trig, True)
		time.sleep(0.00001)
		gpio.output(trig, False)

		while gpio.input(echo) == 0:
			pulseStart = time.time()
		while gpio.input(echo) == 1:
			pulseEnd = time.time()

		pulseDuration = pulseEnd - pulseStart
		distance = pulseDuration * 170
		distance = round(distance, 2)
		if distance < 0.7:
			with picamera.PiCamera() as camera:
				camera.start_preview()
				time.sleep(5)
				camera.stop_preview()
			

		print "Distance = ", distance, "m"
except:
	gpio.cleanup()
		