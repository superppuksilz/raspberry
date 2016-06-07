import module.frontview as frontview
import sensor.light as light
from socket import *
import os
import sys

port = 9001

# sub pi, used in Frontview pi

#fv = frontview.FrontView()
#cam = os.system("raspivid -t 0 -w 320 -h 240 -op 100 -vf -hf -b 500000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.1.2 port=9000")

bright = light.Light()
bright.setLight()

#fv.showView()

svrSock = socket(AF_INET, SOCK_STREAM)

svrSock.connect(('192.168.43.61',9001))

try:

	while True:
		print("start")
		bright.setLight()
		print(bright.getLight())
		if( bright.getLight() < 10 ) :
			print('send')
			svrSock.send(b'00')
		#str = svrSock.recv(1024)
		#if str :
		#    print repr(str)


except Exception as e:
        print ("connection error")
        print (e)







		
