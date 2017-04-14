# pH meter 


## Materials:

* Vernier temperature probe
* Raspberry Pi.
* pH meter.
* Jumpers.
* Chip MCP3008

## Libraries:

```
sudo apt-get install -y python-smbus

sudo apt-get install -y i2c-tools
```
Now change the file 

```
sudo  vi /etc/modules
```

add lines:
```
#i2c-bcm2708&nbsp
#i2c-dev
```
Save changes and close it. Then open the file:
```
sudo vi /etc/modprobe.d/raspi-blacklist.conf
```
Uncomment:
```
dtparam=i2c1=on
dtparam=i2c_arm=on
```

Reboot, test the library:
```
sudo i2cdetect -y 1
```

Check out the physical address and add it to the script.

## Set up:

|From: RGB   | To: Raspberry |
|---|---|
|GND| GND |   
|3V3| 3V3 |
|SDA| SDA|
|SCL| SCL |

## Notes:

* You might need to redefine the physical address.

## References:

* http://bradsrpi.blogspot.com/2013/05/tcs34725-rgb-color-sensor-raspberry-pi.html
* https://github.com/sparkfun/SparkFun_ISL29125_Breakout_Arduino_Library
* https://www.abelectronics.co.uk//kb/article/1/i2c--smbus-and-raspbian-linux
* https://pypi.python.org/pypi/smbus2/0.1.2

