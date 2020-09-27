#!/usr/bin/env python3
import I2C_LCD_driver
from time import *

text = raw_input('Text to display: ')

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string('{}'.format(text), 1)
