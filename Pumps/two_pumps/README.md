# One peristaltic water pumps set-up

This folder contains in `test.py` that turns on and of a 
peristaltic pump contolled by a power relay.

## Materials:

* Raspberry Pi.
* Relay board with at least 2 relays
* 2 Peristalic pump

## Set up:

|From: Raspberry   | To: Relay1   |
|---|---|
|G17| Input |   
|3V3|3V3 |
|GND|GND |


|From: Raspberry   | To: Relay2   |
|---|---|
|G27| Input |   
|3V3|3V3 |
|GND|GND |

|From: Power supply   | To: Pump1/Pump2  |
|---|---|
|+|+ |

|From: Power supply   | To: Relay1/Relay2   |
|---|---|
|-|NO |

|From: Pump1/Pump2  | To: Relay1/Relay2   |
|---|---|
|-|COM |

## Notes:

* Please note that the red dot printed on the peristalic pump 
denotes the positive outlet.
