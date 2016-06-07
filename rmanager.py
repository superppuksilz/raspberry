import module.frontviewCall as frontviewCall
import module.rearview as rearview
import module.emergency as emergency
import module.requestReceiver as reqReceiver
import module.server as server
import sensor.switch as switch
from PIL import Image
import subprocess
import time
from socket import *

server.serv_start()

emerSocket = socket(AF_INET, SOCK_STREAM)
emerSocket.connect(('192.168.43.61',9001))


# main pi, used in Rearview, Bluetooth

fvcall = frontviewCall.FrontViewCall()
rv = rearview.RearView()
emer = emergency.Emergency()


IDLE = 0
FRONT = 1
REAR = 2
EMER = 3

weather = 0

modeStat = IDLE

imgWeather = None

#modeStat = FRONT
swit = switch.Switch()
imgIdle = subprocess.Popen(["display","/home/pi/rraspberry/black.jpg"])        

while True:
    global imgWeather
    modeStat = server.get_status()
    weather = server.get_weather() 
    print(weather)
    if weather == 1 :
        imgWeather = subprocess.Popen(["display","/home/pi/rain.png"])
        server.set_weather(3)
    elif weather == 3 :
        t1 = 0
        t0 = time.clock()
        while( t1  < 3 ):
            t1 = time.clock()-t0
        imgWeather.kill()
        server.set_weather(0)
    elif weather -1 >0 :
        imgWeather = subprocess.Popen(["display","/home/pi/weather_clear.jpg"])
        weather = server.set_weather(3)
        

    if modeStat ==  IDLE or modeStat == REAR:
        modeStat = rv.showView(modeStat)
    elif modeStat == EMER:
	print('emer start')
        imgEmer = subprocess.Popen(["display","/home/pi/rraspberry/emergency.jpg"])
        t0 = time.clock()
        t1 = 0
        while( t1  < 5 ):
            t1 = time.clock()-t0
            swit.checkStat()
            if swit.getStat():
                server.set_status()
                imgEmer.kill()
                swit.changeStat()
                break
        
        if t1 >= 5:
	    emerSocket.send(b'22')
	    server.set_status()
	    imgEmer.kill()
            swit.changeStat()     
    else :
	modeStat = fvcall.showView(modeStat)
