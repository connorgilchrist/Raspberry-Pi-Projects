# Imports
from machine import ADC, Pin
from time import sleep

# Define pin for our sensor
lightsensor = ADC(Pin(26))
    
# Read sensor value and store it in a variable called 'light'
light = lightsensor.read_u16()

# Use the round function to limit the decimal places to 1
lightpercent = round(light/65535*100,1)

# Print our reading and the % symbol
# Convert the reading to a string first using str
print(str(lightpercent) +"%") 