import RPi.GPIO as GPIO
import time

# Variables

delay = 0.5
steps = 50

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Init pins

coil_A_1_pin = 9
coil_A_2_pin = 25
coil_B_1_pin = 11
coil_B_2_pin = 8

# Set pin states

GPIO.setup(coil_A_1_pin, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(coil_A_2_pin, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(coil_B_1_pin, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(coil_B_2_pin, GPIO.OUT,initial=GPIO.LOW)

# Function for step sequence

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)


# Example rotations: forward and backward

for i in range(0, steps):
    setStep(1,0,0,0)
    time.sleep(delay)
    setStep(1,1,0,0)
    time.sleep(delay)
    setStep(0,1,0,0)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,0,1,0)
    time.sleep(delay)
    setStep(0,0,1,1)
    time.sleep(delay)
    setStep(0,0,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)

GPIO.cleanup()     
