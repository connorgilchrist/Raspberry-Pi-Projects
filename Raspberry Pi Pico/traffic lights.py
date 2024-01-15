from machine import Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 0

while counter < 5:
    
    green.value(1)
    amber.value(0)
    red.value(0)

    time.sleep(5)

    green.value(0)
    amber.value(1)
    red.value(0)

    time.sleep(3)

    green.value(0)
    amber.value(0)
    red.value(1)

    time.sleep(5)

    green.value(0)
    amber.value(1)
    red.value(1)

    time.sleep(2)

    green.value(1)
    amber.value(0)
    red.value(0)
    
    counter = counter + 1