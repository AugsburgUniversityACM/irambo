#!/usr/bin/python3
import time

x=open('/dev/ttyUSB0','wb')
x.write(bytes([
    # Header
    128, # Start OI
    131, # OI Safe Mode

    # Commands
    139, # LED
    0, # Turn off All Lights
    # int('00001111', 2), # Turn on All lights (Check robot, Dock, Spot, Debris)
    0,
    0,
]))

time.sleep( 5 )

x.write(bytes([
    # Footer
    173, # Stop OI
]))
x.close()
