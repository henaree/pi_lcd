# pi_lcd

## Introduction
This is a quick run through of how to get a raspberry pi outputting its cpu temp and/or IP address to an i2c LCD screen.

## Parts List
- LCD Display
- I2C extender (LCM1602 IIC)
- Raspberry pi

## Setup

### Pi & LCD Setup

Connect the HPIO pins of the raspberry pi to the I2C extender as follows:

- Pin 3 GPIO 2 (I2C1 SDA) 	- SDA
- Pin 4 5v Power		  	- VCC
- Pin 5 GPIO 3 (I2C1 SCL) 	- SCL
- Pin 6 Ground 				- GND

![](https://raw.githubusercontent.com/henaree/pi_lcd/master/RPi_i2C_LCD_bb.png)
### I2C Setup

- Install the needed tools
```bash
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
```

- Enable kernel support

```bash
sudo raspi-config
```
1. Interfacing Options (Advanced on older versions)
2. I2C
3. Enable

Then reboot

## Testing

Check to see if I2C is working and devices are detected:
```bash
sudo i2cdetect -y 1
```

## The scripts

Included in the ```scripts``` directory are these python scripts:
- I2C_LCD_driver.py
	- driver for the pi to communicate with the screen via I2C
- hello_world.py
	- Displays Hello World! on the LCD
- ip_address.py
	- Displays ip address of wlan
- display_temp.py 
	- Updates the screen with the latest temperature of the CPU of the pi

To update the LCD screen, simply run the desired script, for example ```python display_temp.py``` will run the temperature script. In the temperature scripts case, pressing ```ctrl + C``` will cancel the script from running as the script loops to update the temperature over time.

#### TODO
- ~~Tidy up cpu temp output text~~
- ~~make hello world interactive~~
- ~~improve ip_address to detect what device is in use (ethernet/wlan) and display that ip~~
- combine ip_address, display_temp
- make interctive script to choose what to display
