from machine import Pin, PWM
import time, sys, random

beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(13))
buzzer.freq(1000)
buzzer.duty_u16(0)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

def flash(red_value, amber_value, green_value, vol, length, delay):
    red.value(red_value)
    amber.value(amber_value)
    green.value(green_value)
    buzzer.duty_u16(vol)
    time.sleep(length)
    buzzer.duty_u16(0)
    time.sleep(delay)
   
start_time = 0
f1_reaction = 160

#print('Are you ready for the reaction game?')
#time.sleep(3)
#print('Tap the desk as quickly you can when the green light shows...')
#time.sleep(5)

randomstart = random.uniform(0, 5)

flash(1, 1, 1, 1000, 1, 1)
flash(1, 1, 0, 1000, 1, 1)
flash(1, 0, 0, 1000, 1, randomstart)
buzzer.freq(2000)
print('GO!')

start_time = time.ticks_ms()
red.value(0)
buzzer.duty_u16(1000)

while True:
    time.sleep(0.00000001)
    
    if beam.value() == 0:
        reactiontime = time.ticks_ms() - start_time
        f1_diff = reactiontime - f1_reaction
        buzzer.duty_u16(0)
        print('Good job!')
        print(f'Your reaction time was {reactiontime} milliseconds.')
        time.sleep(1.5)
        print(f'That is {f1_diff} milliseconds slower than Michael Schumacher')
        sys.exit()
        
        
        
        
        
        
        
        