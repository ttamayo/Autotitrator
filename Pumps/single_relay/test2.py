import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)      
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

for i in range(3):
    GPIO.output(17,1)
    print('I am i printing 17')
    sleep(20)
    GPIO.output(17,0)
    sleep(2)
    GPIO.output(27,1)
    print('I am i printing 27')
    sleep(20)
    GPIO.output(27,0)
    sleep(2)
    GPIO.output(27,1)
    GPIO.output(17,1)
    print('I am i printing 27 and 17')
    sleep(20)
    GPIO.output(27,0)
    GPIO.output(17,0)


    

GPIO.cleanup()
