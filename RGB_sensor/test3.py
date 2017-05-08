import smbus
import time
import matplotlib.colors as colors
import numpy as np
import matplotlib.pyplot as plt

class RGB_sensor(object):
   def __init__(self):
      self.bus = smbus.SMBus(1)
      # I2C address 0x29
      # Register 0x12 has device ver. 
      # Register addresses must be OR'ed with 0x80
      self.bus.write_byte(0x29,0x80|0x12)
      ver = self.bus.read_byte(0x29)
      # version # should be 0x44
      if ver == 0x44:
        self.bus.write_byte(0x29, 0x80|0x00) # 0x00 = ENABLE register
        self.bus.write_byte(0x29, 0x01|0x02) # 0x01 = Power on, 0x02 RGB sensors enabled
        self.bus.write_byte(0x29, 0x80|0x14) # Reading results start register 14, LSB then MSB
      else: 
         print "Device not found\n"

   def rgb_sample(self):  
        data = self.bus.read_i2c_block_data(0x29, 0)
        clear = clear = data[1] << 8 | data[0]
        red = data[3] << 8 | data[2]
        green = data[5] << 8 | data[4]
        blue = data[7] << 8 | data[6]
        print(clear)
        self.rgb = np.array([1.0*red/clear,1.0*green/clear,1.0*blue/clear])
        return self.rgb

   def string_hex(self):
       string = ''
       for i in self.rgb:
           string += hex(int(i*256))[2:]
       return string


rgb_sensor = RGB_sensor()
while True:
    print rgb_sensor.rgb_sample()
    print rgb_sensor.string_hex()
    plt.imshow([[rgb_sensor.rgb_sample()]])
    plt.pause(0.01)
    time.sleep(1)
