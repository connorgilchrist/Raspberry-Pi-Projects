# Imports
from machine import Pin
import time

#Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1 # Set the counter to 1

while counter < 100: # While count is less than 11
    
    print(counter) # Print the current counter
    
    # Red ON
    red.value(1) # ON
    amber.value(0) # OFF
    green.value(0) # OFF
    
    time.sleep(0.1) # Wait half a second
    
    # Amber ON
    red.value(0) # OFF
    amber.value(1) # ON
    green.value(0) # OFF
    
    time.sleep(0.1) # Wait half a second
    
    # Green ON
    red.value(0) # OFF
    amber.value(0) # OFF
    green.value(1) # ON
    
    time.sleep(0.1) # Wait half a second
    
    counter += 1 # Add 1 to our counter