import sensor.light as light

li = light.Light()

while True:
       li.setLight()
       print li.getLight()
		
