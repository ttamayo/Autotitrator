import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)      
direction = 20
step = 21
GPIO.setup(int(direction),GPIO.OUT) # Direction
GPIO.setup(step,GPIO.OUT) # Step



#### Setting up direction
rotation = 'left'

if rotation == 'left':
    GPIO.output(int(direction),True)
else:
    GPIO.output(direction,False)


#### Steps

for i in range(100):
    GPIO.output(step,True)
    sleep(0.5)
    GPIO.output(step,False)
    sleep(0.5)

    

    

GPIO.cleanup()
