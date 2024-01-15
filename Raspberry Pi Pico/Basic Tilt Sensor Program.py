# Imports
from machine import Pin
import time

# Set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True: # Run forever

    time.sleep(0.01) # Short delay
    
    if tilt.value() == 1: # If sensor is HIGH

        print("I tilted!") # Print a string
