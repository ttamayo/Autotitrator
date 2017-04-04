import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)      
GPIO.setup(17,GPIO.OUT)

for i in range(3):
    GPIO.output(17,1)
    sleep(20)
    GPIO.output(17,0)
    sleep(2)
    

GPIO.cleanup()
