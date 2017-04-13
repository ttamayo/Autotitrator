from gpiozero import MCP3008
import RPi.GPIO as GPIO
import time
import numpy as np


'''https://learn.sparkfun.com/tutorials/vernier-shield-hookup-guide?_ga=1.200530086.94916921.1488849082#resources-and-going-further'''

### Controling vernier shield
GPIO.setmode(GPIO.BCM)  ## Enable Boardcom numbers
GPIO.setup(05,GPIO.OUT,initial=GPIO.LOW) ## We set up the GPIO pin 17 Turned off
GPIO.setup(06,GPIO.OUT,initial=GPIO.LOW) ## We set up the GPIO pin 17 Turned off
GPIO.output(05,0) ## We'll use Serial 1 of Vernier shield
GPIO.output(06,0) 

pot = MCP3008(0) ## assuming we used A0 form 0 to 5V
                 ## If we excpect form -10 to 10 use 1
print("current value",pot.value) ## It should be between 1 and 0
refvoltage = 3.3

for i in range(3):
   # 3 samples
   time.sleep(5) ## we need to take values in certain intervals
   rawAnalogReading = pot.value
   print(pot.value)

GPIO.cleanup()    
