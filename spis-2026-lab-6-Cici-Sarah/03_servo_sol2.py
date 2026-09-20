# This program demonstrates how to control a servo

# Import the relevant libraries
import RPi.GPIO as GPIO
import time
 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# set GPIO Pins
ServoPin = 25                                       # GPIO pin for the servo

# set GPIO direction (IN / OUT)
GPIO.setup(ServoPin, GPIO.OUT)                      # Set ServoPin's mode to output

# Set GPIO Pins
LedPin = 16                                     # GPIO pin for the LED
BtnPin = 20                                     # GPIO pin for the button

# Set GPIO direction (IN / OUT)
GPIO.setup(LedPin, GPIO.OUT)                            # Set LedPin's mode to output
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Set BtnPin's mode is input, and pull up to high level (3.3V)

# Start conditions
GPIO.output(LedPin, GPIO.LOW)                   # Set LedPin low to turn the led off 

# The servo is controlled using Pulse Width Modulation (PWM)
# The next few lines of code take care of the required setup for this functionality
# The details are not important; you should not modify this code
# --- Start of the PWM setup ---
# Set PWM parameters
pwm_frequency = 50
duty_min = 2.5 * float(pwm_frequency) / 50.0
duty_max = 12.5 * float(pwm_frequency) / 50.0

# Helper function to set the duty cycle
def set_duty_cycle(angle):
    return ((duty_max - duty_min) * float(angle) / 180.0 + duty_min)

# Create a PWM instance
pwm_servo = GPIO.PWM(ServoPin, pwm_frequency)

# --- End of the PWM setup ---

delayTarget = 1
LastTime = time.time()
i = 0

# Main program 
try:
        
    # This code repeats forever
    while True:
        button = GPIO.input(BtnPin)
        if button == 1:
            GPIO.output(LedPin, GPIO.LOW)
                
            # Check the current time
            currentTime = time.time()
            if (currentTime - LastTime > delayTarget and i%2==0):
                # Move the servo
                angle = 0
                pwm_servo.start(set_duty_cycle(angle))
                print ("Moving to angle 0")
                LastTime = currentTime
                i+=1
            currentTime = time.time()
            
            if (currentTime - LastTime > delayTarget and i%2 == 1):  
                angle = 180
                pwm_servo.start(set_duty_cycle(angle))
                print ("Moving to angle 180")
                LastTime = currentTime
                i+=1
            
        else:
            GPIO.output(LedPin, GPIO.HIGH)
            pwm_servo.start(set_duty_cycle(0))
        print(button)
        

            
# Reset by pressing CTRL + C
except KeyboardInterrupt:
        print("Program stopped by User")
finally:
        GPIO.cleanup()
