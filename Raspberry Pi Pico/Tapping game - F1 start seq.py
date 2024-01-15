# Imports
from machine import Pin, PWM
import time, sys

# Set up LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up the Break Beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set buzzer PWM frequency to 1000
buzzer.freq(1000)

# Start with the buzzer volume off (duty 0)
buzzer.duty_u16(0)

# Create game variables
starttime = 0
timecheck = 0
scorecounter = 0
state = 0
targetscore = 150

def LED(red_value, amber_value, green_value):
    red.value(red_value)
    amber.value(amber_value)
    green.value(green_value)

def start_seq():
    red.value(1)
    amber.value(1)
    green.value(1)
    buzzer.duty_u16(10000)
    
    time.sleep(0.5)
    
    buzzer.duty_u16(0)
    
    time.sleep(0.5)
    
    green.value(0)
    buzzer.duty_u16(10000)
    
    time.sleep(0.5)

    buzzer.duty_u16(0)
    
    time.sleep(0.5)
    
    amber.value(0)
    buzzer.duty_u16(10000)
    
    time.sleep(0.5)

    buzzer.duty_u16(0)
    
    time.sleep(0.5)
    
    red.value(0)
    buzzer.freq(2000)
    buzzer.duty_u16(10000)
    
    time.sleep(0.3)
    
    buzzer.duty_u16(0)
    buzzer.freq(1000)
    
def flash_finish():
            red.value(1)
            amber.value(1)
            green.value(1)
            buzzer.duty_u16(10000)
            time.sleep(0.2)
            red.value(0)
            amber.value(0)
            green.value(0)
            buzzer.duty_u16(0)
            time.sleep(0.2)
            

print("Game starts after the sequence....")
time.sleep(3)
start_seq()

print("It's lights out and away we go!")

print("-------------------------------")

# Store our start time (seconds)
starttime = time.time()

while True: # Run this block until code stopped

    time.sleep(0.0001) # Very short delay

    # Take the current time and minus the original start time
    # This gives us the number of seconds since we started the game
    timecheck = time.time() - starttime

    if timecheck >= 30: # If 30 or more seconds have passed
                
        # LEDs off
        red.value(0)
        amber.value(0)
        green.value(0)
        
        # Beep to signal game end
        buzzer.freq(200)
        buzzer.duty_u16(10000)
        time.sleep(0.2)
        buzzer.freq(150)
        time.sleep(0.5)
        buzzer.duty_u16(0)
        
        # Print the target and player's score
        print("-------------------------------")
        print("GAME OVER! YOU LOSE :(")
        print("The target was",targetscore,", you scored",scorecounter)
        print("-------------------------------")
        
        # Exit the program
        sys.exit()
        
    elif scorecounter >= targetscore: # If player's score has hit the target      
        flashcount =  0
        while flashcount < 5:
            flash_finish()
            flashcount = flashcount + 1
        
        # Print time taken to win
        print("-------------------------------")
        print("YOU WIN!")
        print("You took",timecheck,"seconds!")
        print("-------------------------------")
        
        # Exit the program
        sys.exit()
   
    elif state == 0 and beam.value() == 0: # If state is 0 AND our pin is LOW
        
         scorecounter = scorecounter + 1 # Add +1 to our score counter
        
         state = 1 # Change state to 1
        
         print("SCORE =",scorecounter,"/",targetscore) # Print the score and target
         print("Time remaining:", (30 - timecheck)) # take our timecheck variable away from 30 - gives the remaining time
         
         if scorecounter < (targetscore / 100 * 50): # If our score is less than 33% of the target
             
            red.value(1) # Red LED on
            amber.value(0)
            green.value(0)
            
         elif (targetscore/ 100 * 50) < scorecounter < (targetscore / 100 * 80): # If our score is between 33% and 66% of the target
             
            red.value(1) # Red LED on
            amber.value(1) # Amber LED on
            green.value(0)
            
         elif scorecounter > (targetscore / 100 * 80): # If our score is over 66% of the target
            
            red.value(1) # Red LED on
            amber.value(1) # Amber LED on
            green.value(1) # Green LED on
        
    elif state == 1 and beam.value() == 1: # If state is 1 AND our pin is HIGH
                        
        state = 0 # Change the state to 0
