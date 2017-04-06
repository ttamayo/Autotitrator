# One pump

This folder contains in `test.py` a test
of a pump to move by a motor driver in two speeds (back and forward).

## Materials:

* Raspberry Pi
* Motor driver
* 12V peristaltic pumps.

## Warnings!

* CONNECT it to the 3V3 pin. DO NOT USE 5V!!
* Don't forget to add the heat disipear.
* Make sure is located in a ventilated area, it can get very hot.

## Set up:
|From: Raspberry   | To: Driver   |
|---|---|
|G17| MS1|   
|G27| MS2|
|G22| MS3|
|G05| Dir|
|VDD| 3V3 |
|GND| GND|


|From: Driver   | To: Power Supply  |
|---|---|
|VMOT| + |   
|GND | - |

|From: Driver   | To: Pump  |
|2B  | B+|
|2A  | A+|
|1A  | A-|
|1B  | B-|



## References:

