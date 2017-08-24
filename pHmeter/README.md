# pH meter 

There are 2 possible set-ups.

1) Vernier phMeter
2) Circuit with i2c protocol

# 1. Vernier

Note, it is the same set up as the thermometer.

## Materials:

* Vernier temperature probe
* Raspberry Pi.
* pH meter.
* Jumpers.
* Chip MCP3008

## Set up:

|From: Raspberry   | To: MCP3008 (left) |
|---|---|
|3V3| 8 |   
|GND|3 |
|3V3| 1 |
|3V3| 2 |
|MISO| 4 |
|GP09| 5 |
|SCLC| 6 |
|CE0| 7 |


|From: Vernier Sensor | To: Raspberry  |
|---|---|
|5V | 5V |
|3.3V | 3.3V |   
|GND | GND | 
|GND | GND | 

|From: Vernier Sensor   | To: MCP3008 (right) |
|---|---|
|A1 | 0 |   
|A2 | 1 |   


## Notes:

* Please note that the small hole should be pointing towards the upper part. (See notebook).
* (as always) Double check the wiring of any circuit you set up before connecting the circuit to a power source. Triple check if your circuit includes any chip!
* Check the temperature of the chip - there is a chance that you will burn it, which is bad for your experimental setup.
* Be careful with the chip. Pins tend to break when touched with bare hands, or even just stared at for too long 


# 2. Atlas scientific

https://myhydropi.com/connecting-a-ph-sensor-to-a-raspberry-pi

References:

https://stevieb9.github.io/rpi-adc-mcp3008/datasheet/MCP3008.pdf
