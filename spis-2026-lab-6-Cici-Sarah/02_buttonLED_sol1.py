# This program demonstrates how to read a button
# It will use this information to control an LED

# Import the relevant libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Set GPIO Pins
LedPin = 16                                     # GPIO pin for the LED
BtnPin = 20                                     # GPIO pin for the button

# Set GPIO direction (IN / OUT)
GPIO.setup(LedPin, GPIO.OUT)                            # Set LedPin's mode to output
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Set BtnPin's mode is input, and pull up to high level (3.3V)

# Start conditions
GPIO.output(LedPin, GPIO.LOW)                   # Set LedPin low to turn the led off 



# Main program 
try:

    # This code repeats forever
    while True:
                
        button = GPIO.input(BtnPin)
        if button == 1:
            GPIO.output(LedPin, GPIO.LOW)
        else:
            GPIO.output(LedPin, GPIO.HIGH)   
        print(button)

        # Slow the loop down. Without this the loop prints ~500,000 lines/second,
        # which makes the Thonny shell unusable and pegs a CPU core.
        time.sleep(0.1)


# Reset by pressing CTRL + C
except KeyboardInterrupt:              
        print("Program stopped by User")
finally:
        GPIO.output(LedPin, GPIO.LOW)          	# LED off
        GPIO.cleanup()                          # Release resource

