import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)      
GPIO.setup(17,GPIO.OUT) # Direction
GPIO.setup(27,GPIO.OUT) # Step



#### Setting up direction
direction = 'left'

if direction== 'left':
    GPIO.output(27,True)
else:
    GPIO.output(27,False)


#### Steps

for i in range(10):
    GPIO.output(17,True)
    sleep(10)
    GPIO.output(27,False)
    sleep(10)

    

    

GPIO.cleanup()
