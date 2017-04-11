from gpiozero import MCP3008
import time
import numpy as np


'''https://learn.sparkfun.com/tutorials/vernier-shield-hookup-guide?_ga=1.200530086.94916921.1488849082#resources-and-going-further'''


def resistance(rawAnalogInputs):
  '''
  /* function to convert the raw Analog Input reading to a resistance value    
   * Schematic:
   *   [Ground] -- [thermistor] -------- | -- [15,000 ohm bridge resistor] --[Vcc (5v)]
   *                                     |
   *                                Analog Pin 0
   *
   * For the circuit above:
   * Resistance = ((rawAnalogInput*15000) /(1023 - rawAnalogInput))
   */
   '''
  temp = (rawAnalogInput * 15000) / (1023 - rawAnalogInput)
  return temp # returns the value calculated to the calling function.

def steinharthart(resistance):
   '''
   // function users steinhart-hart equation to return a temperature in degrees celsius. 
   /* Inputs ADC count from Thermistor and outputs Temperature in Celsius
   * There is a huge amount of information on the web about using thermistors with the Arduino.
   * Here we are concerned about using the Vernier Stainless Steel Temperature Probe TMP-BTA and the 
   * Vernier Surface Temperature Probe STS-BTA, but the general principles are easy to extend to other
   * thermistors.
   * This version utilizes the Steinhart-Hart Thermistor Equation:
   *    Temperature in Kelvin = 1 / {A + B[ln(R)] + C[ln(R)]^3}
   *   for the themistor in the Vernier TMP-BTA probe:
   *    A =0.00102119 , B = 0.000222468 and C = 1.33342E-7
   *    Using these values should get agreement within 1 degree C to the same probe used with one
   *    of the Vernier interfaces
   * 
   */ '''
  logRes = np.log(resistance) 
  k0 = 0.00102119
  k1 = 0.000222468
  k2 = 0.000000133342

  temp = 1 / (k0 + k1 * logRes + k2 * logRes*logRes*logRes)
  temp = temp - 273.15 #  convert from Kelvin to Celsius 
  return temp

if __name__ == 'main':
   pot = MCP3008(0) ## assuming we used A0
   print("current value",pot.value) ## It should be between 1 and 0
   phSense = 0
   refvoltage = 1.1

   for i in range(10):
      # 10 samples
      time.sleep(10) ## we need to take values in certain intervals
      rawAnalogReading = pot.value
      thermistor = resistance(rawAnalogReading) # converts raw analog value to a resistance
      Temp = steinharthart(thermistor) # applies the Steinhart-hart equation
      print(Temp)
