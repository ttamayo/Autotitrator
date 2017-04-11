# Thermometer

This folder contains in `test.py` that obtains the signal ofturns on and off a 
peristaltic pump contolled by a power relay.

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
|3V3|7 |
|GND| 1 |
|GND| 2 |
|GP10| 2 |
|GP09| 4 |
|GP11| 5 |
|GP8| 2 |


|From: Vernier Sensor | To: Raspberry  |
|---|---|
|5V | 5V |

|From: Vernier Sensor   | To: MCP3008 (right) |
|---|---|
|3.3V | 3.3V |   
|GND | GND |   
|AO | 7 |   
|AO | 9 |   

## Notes:

* Please note that the small hole should be pointing towards the upper part. (See notebook).
* Double check before clossing any circuit the wires, specially with the chip.
* Check out the temperature of the chip (or not), it is possible that you burn it.
* Be careful with the chip, do not handdle directly with the hands all pins.
