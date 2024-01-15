# Imports
from machine import ADC, Pin
from time import sleep

# Define pin for our sensor
lightsensor = ADC(Pin(26))
    
# Read sensor value and store it in a variable called 'light'
light = lightsensor.read_u16()

# Turn our reading into a percentage of the analogue range
lightpercent = light/65535*100
    
print(lightpercent)
