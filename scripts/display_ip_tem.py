#!/usr/bin/env python3

import I2C_LCD_driver #import I2C LCD driver
from subprocess import Popen, PIPE
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

#initilise LCD screen
mylcd = I2C_LCD_driver.lcd()

# looking for an active Ethernet or WiFi device
def find_interface():
    find_device = "ip addr show"
    interface_parse = run_cmd(find_device)
    for line in interface_parse.splitlines():
        if "state UP" in line:
            dev_name = line.split(':')[1]
    return dev_name

# find an active IP on the first LIVE network device
def parse_ip():
    find_ip = "ip addr show %s" % interface
    find_ip = "ip addr show %s" % interface
    ip_parse = run_cmd(find_ip)
    for line in ip_parse.splitlines():
        if "inet " in line:
            ip = line.split(' ')[5]
            ip = ip.split('/')[0]
    return ip

# run unix shell command, return as ASCII
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')

# before we start the main loop - detect active network device and ip address
sleep(2)
interface = find_interface()
ip_address = parse_ip()

while True:
        cpu_temp()
        mylcd.lcd_display_string(" {}".format(ip_address), 2)
