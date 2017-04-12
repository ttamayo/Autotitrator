# One steeper peristalic water pump set-up

This folder contains in `test.py` that turns on and off a 
stepper peristaltic pump contolled by a chip L293D.

## Materials:

* Raspberry Pi.
* Chip L293D.
* Peristalic pump


## Set up:

|From: L293D   | To: Power supply   |
|---|---|
|1| + |   
|4| - |   
|5| - |   
|12| - |   
|13| - |   
|9|+ |

|From: L293D   | To: Raspberry Pi    |
|---|---|
| 2| G17 |
| 7| G22|
| 15|G23 |
| 10|G24 |

|From: L293D   | To: Pump   |
|---|---|
| A+ | 3|
| A- | 6|
| B+ | 14|
| B- | 10|

## Notes:

* Please note that the small circle should be pointing up.
