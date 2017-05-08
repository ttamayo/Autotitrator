import smbus2 
from smbus2 import SMBus
from smbus2 import SMBusWrapper
import time
import numpy as np
import matplotlib.pyplot as plt

'''
Connections

TCS34725  RPi
SDA       P3 GPIO 0 (SDA)
SCL       P5 GPIO 1 (SCL)
3V3       P1 3V3
GND       P9

source: http://bradsrpi.blogspot.com/2013/05/tcs34725-rgb-color-sensor-raspberry-pi.html'''

class RGB(object):
    def __init__(self):
       self.bus = SMBus(1)
  
       ## Checking device
       device = self.bus.read_byte_data(0x44,0) ## Read device

       ## init data
       self.wire = Data(0x44,self.bus) 
    
       ### Reset registers
       if not(self.reset()):
          print ('We failed in resetting')
          return

       if not(self.config()):
          print ('We failed in confg')
          return 
       print 'We successfully configured the sensor'
       return 
    
    def config(self):
       print 'Here'
       self.wire.write(0x01,0x05|0x08)
       self.wire.write(0x02,0x3F)
       self.wire.write(0x03,0x00)
 
       data = self.wire.read(0x01) ## Lux and RGB
       print 'data',data
       if (data != 0x05|0x08):
          return False
       data = self.wire.read(0x02) ## IR 
       if (data != 0x3F): 
          return False
       data = self.wire.read(0x03) ## CFG defaul
       if (data != 0x00):
          return False
       return True
      
    def reset(self):
       self.wire.write(0x01)
       self.wire.write(0x02)
       self.wire.write(0x03)
       data = self.wire.read(0x08) ## Read device
       if data != 0x00: # version # should be 0x00
          return False
       else:
          return True

    def Red(self):
        return  self.wire.read(0x0B) ## Red
    
    def Green(self):
        return  self.wire.read(0x09) ## Green
    
    def Blue(self):
        return  self.wire.read(0x0D) ## Blue


    def close(self):
        self.bus.close()
        return
    
class Data(object):
    def __init__(self,address,bus):
        self.address = address
        self.bus = bus
        return

    def read(self,reg,size=True):
       if size:
          return  self.bus.read_byte_data(self.address,reg) 
       else:
          return bus.read_i2c_block_data(self.adress, reg, 16) 
 
    def write(self,reg,data=0x00):
       if data:
         self.bus.write_byte_data(self.address,reg,data) 
       else:
          self.bus.write_byte_data(self.address,reg,data) 
       return
       
          

   
rgb_sensor = RGB()
g = rgb_sensor.Green()
r = rgb_sensor.Red()
b = rgb_sensor.Blue()
print(r, g, b)
#color = np.array((r,g,b))
#plt.plot(domain,values,color = color/255., lw = 10)
#plt.show()
rgb_sensor.close()

