# Imports
from machine import ADC, Pin

# Define pin for our sensor
lightsensor = ADC(Pin(26))

# Read sensor value and store it in a variable called 'light'
light = lightsensor.read_u16()

# print the value
print(light)
