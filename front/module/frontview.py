import subprocess
import os
import sys

class FrontView:
    cam = 0

    def __init__(self):
        cam = 0

    def showView(self):

#	cmd = ["raspivid", "-t", "0", "-w", "320", "-h", "240" ,"-vf", "-hf", "-b" ,"500000" ,"-o" ,"-" ,"|", "gst-launch-1.0" ,"-v" ,"fdsrc","!" ,"h264parse" ,"!" ,"rtph264pay" ,"config-interval=1" ,"pt=96" ,"!" ,"gdppay" ,"!" ,"tcpserversink" ,"host=192.168.1.2" ,"port=9000"]
	self.cam = os.system("raspivid -t 0 -w 320 -h 240 -op 100 -vf -hf -b 500000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.1.2 port=9000")


        

