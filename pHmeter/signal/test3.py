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

pot2 = MCP3008(4) ## assuming we used A0 form 0 to 5V
                 ## If we excpect form -10 to 10 use 1
print("current value",pot2.value) ## It should be between 1 and 0
refvoltage = 3.3

n_measurements = 10
samples = int(input('Number of samples'))
pHs = np.zeros(samples)
potentials = np.zeros((samples,n_measurements))
for j in range(samples):
   pH = input('Enter pH ')
   pHs[j] = pH
   for i in range(n_measurements):
      potentials[j,i] = pot2.value  

#for i in range(3):
   # 3 samples 
      time.sleep(1) ## we need to take values in certain intervals
  
#rawAnalogReading = pot.value
print(pHs)
print(potentials)
np.savetxt('calibration_pHs3', pHs)
np.savetxt('calibration_potentialspH3', potentials)
GPIO.cleanup()    
