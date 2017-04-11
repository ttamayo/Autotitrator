# One steeper peristalic water pump set-up

This folder contains in `test.py` that turns on and off a 
stepper peristaltic pump contolled by a chip L293D.

## Materials:

* Raspberry Pi.
* Chip L293D.
* Peristalic pump
*  


## Set up:

|From: Pump   | To: Chip   |
|---|---|
|G17| Input |   
|3V3|3V3 |
|GND|GND |

|From: Power supply   | To: Dhip   |
|---|---|
|+|+ |

|From: Power supply   | To: Relay   |
|---|---|
|-|NO |

|From: Pump  | To: Relay   |
|---|---|
|-|COM |

## Notes:

* Please note that the red dot printed on the peristalic pump 
denotes the positive outlet.
