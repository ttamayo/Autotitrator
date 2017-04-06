import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)   # Enable boardcom numbers
GPIO.setup(17,GPIO.OUT)  # Setting pump 1 to 17
GPIO.setup(27,GPIO.OUT)  # Setting pump 2 to 27

for i in range(3):     
    GPIO.output(17,1)
    print('I am turning on 17')
    sleep(20)
    print('I am turning off 17')
    GPIO.output(17,0)
    sleep(20)
    print('I am turning on 27')
    GPIO.output(27,1)
    sleep(20)
    print('I am turning off 27')
    GPIO.output(27,0)
    sleep(20)
    print("I am turining on 27 and 17")
    GPIO.output(27,1)
    GPIO.output(17,1)
    sleep(20)
    print("I am turining off 27 and 17")
    GPIO.output(27,0)
    GPIO.output(17,0)


    

GPIO.cleanup()
