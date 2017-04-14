# Thermometer

This folder contains in `test.py` that obtains the signal
of a themperature/pHprobe.

## Materials:

* Vernier temperature probe
* Raspberry Pi.
* Vernier Sensor Interface Shield.
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
* Double check before clossing any circuit the wires, specially with the chip.
* Check out the temperature of the chip (or not), it is possible that you burn it.
* Be careful with the chip, do not handdle directly with the hands all pins.
