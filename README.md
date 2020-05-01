# brematic_gwy_433_python

Basic command line tool to switch 433 MHz receivers through a Brematic GWY 433 written in Python

There is a python script switch.py that you have to call with 3 or 4 parameters:
system-code, unit-code, on/off, gateway ip (optional)

system- and unit-code are both 5-digit binary codes, that resemble the DIP switches in your receivers.
"System" ist the one with 1-5, "Unit" is the one usually with A-E.

The third parameter is the word "on" or "off"

Before you can use this script, you should to edit the script, and put in the IP-address of your gateway. It is also possible to define the IP-address of the gateway as the fourth command line parameter.

So `IP = "192.168.0.123"` in line 8 of switch.py has to change to the IP of your gateway. I recommend to set the address of your gateway by DHCP to a fixed IP.

This little Python script has no external dependencies. Everything should be already in your Python distribution
