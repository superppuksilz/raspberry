import sensor.switch as switch
import module.server as server 
import subprocess

class FrontViewCall:
    swit = switch.Switch()
    cam = 0
    camStatus = 0

    def __init__(self):
        swit = switch.Switch()
        cam = 0
        camStatus = 0

    def showView(self, stat):
        self.swit.checkStat()

        # need to get status
        
        if not self.swit.getStat():
            if (stat and self.camStatus == 0) :
                cmd = ["gst-launch-1.0", "-v", "tcpclientsrc", "host=192.168.43.162", "port=9000", "!", "gdpdepay", "!", "rtph264depay", "!", "avdec_h264", "!", "videoconvert", "!", "ximagesink", "sync=false"]
                
                self.cam = subprocess.Popen(cmd, shell=False)
                print("test")
                self.camStatus = 1
                stat = 1

        else:
            if self.camStatus == 1:
                self.cam.kill()
                self.camStatus = 0
                stat = 0
                server.set_status()
        self.swit.changeStat()
        return stat;



		
