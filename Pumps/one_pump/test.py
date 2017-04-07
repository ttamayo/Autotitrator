import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)  ## Enable Boardcom numbers
GPIO.setup(17,GPIO.OUT,initial=RPIO.LOW) ## We set up the GPIO pin 17 Turned off

for i in range(3):    ## We do 3 iterations
    GPIO.output(17,1) ## Turn on
    sleep(20)         ## wait 20 secs
    GPIO.output(17,0) ## Turn off
    sleep(2)
    
GPIO.cleanup()        ## Don't forget to close the port
