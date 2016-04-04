import sensor.switch as switch
import time

sw = switch.Switch()
while True:
       time.sleep(0.5)
       sw.checkStat()
       print sw.getStat()
       sw.changeStat()
 
		
