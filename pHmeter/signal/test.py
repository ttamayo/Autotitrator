from gpiozero import MCP3008
import time
import numpy as np


'''
References:
http://forum.arduino.cc/index.php?topic=96070.0
https://learn.sparkfun.com/tutorials/vernier-shield-hookup-guide?_ga=1.200530086.94916921.1488849082#resources-and-going-further'''


if __name__ == 'main':
   pot = MCP3008(0) ## assuming we used A0
   print("current value",pot.value) ## It should be between 1 and 0
   phSense = 0
   refvoltage = 1.1

   tmp = 0.0
   for i in range(20):
      # 10 samples
      time.sleep(10) ## we need to take values in certain intervals
      rawAnalogReading = pot.value
      tmp += rawAnalog ## sampling 20 times
 
   signal = 5.0 * tmp (1023*samples)
   print ("Analog reading &f"%tmp)
