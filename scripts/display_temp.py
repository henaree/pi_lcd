#!/usr/bin/env python3

import I2C_LCD_driver #import I2C LCD driver
import os #import operating system functions
import time #imports time function
from time import sleep #imports sleep function from time function

mylcd = I2C_LCD_driver.lcd() # initalise LCD display

#CPU temp function
def cpu_temp():
        for _ in range(10):
                temp = os.popen("vcgencmd measure_temp").readline() #get temp reading

                mylcd.lcd_display_string(" CPU {}".format(temp), 1) #prints temp on LCD

                sleep(1) #sleeps for (x) seconds before restarting loop

while True:
        cpu_temp()
