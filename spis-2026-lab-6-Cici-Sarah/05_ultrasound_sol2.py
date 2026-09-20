# This program demonstrates how to control an ultrasound distance sensor

# Import the relevant libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# set GPIO Pins
TriggerPin  = 18
EchoPin     = 24
 
# set GPIO direction (IN / OUT)
GPIO.setup(TriggerPin, GPIO.OUT)
GPIO.setup(EchoPin, GPIO.IN)

# Wait for sensor to settle
GPIO.output(TriggerPin, False)
print("Waiting for sensor to settle")
time.sleep(2)
print("Start sensing")

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

# Helper function to get the distance from the ultrasound sensor.
# It returns the measured distance in cm or -1 if it doesn't detect anything nearby.
# The function can take up to 0.25 seconds to execute.
# The details are not important; you should not modify this code
# --- Start of the ultrasound sensor helper function ---
def distance():
    
    # Create a pulse on the trigger pin
    # This activates the sensor and tells it to send out an ultrasound signal
    GPIO.output(TriggerPin, True)
    time.sleep(0.00001)
    GPIO.output(TriggerPin, False)

    # Wait for a pulse to start on the echo pin
    # The response is not valid if it takes too long, and we should break the loop
    valid = True
    RefTime = time.time()
    StartTime = RefTime
    while (GPIO.input(EchoPin) == 0) and (StartTime-RefTime < 0.1):
        StartTime = time.time()
    if (StartTime-RefTime >= 0.1):
        valid = False
        
    # Wait for a pulse to end on the echo pin
    # The response is not valid if it takes too long, and we should break the loop
    if (valid):
        RefTime = time.time()
        StopTime = time.time()
        while (GPIO.input(EchoPin) == 1) and (StopTime-RefTime < 0.1):
            StopTime = time.time()
        if (StopTime-RefTime >= 0.1):
            valid = False
        
    # If we received a complete pulse on the echo pin (i.e., valid == True)
    # Calculate the distance based on the length of the echo pulse and
    # the speed of sound (34300 cm/s)
    if (valid):
        EchoPulseLength = StopTime - StartTime
        return (EchoPulseLength * 34300) / 2        # Divide by 2 because we are calculating based on a reflection, so the travel time there and back
    else:
        return -1
        
# --- End of the ultrasound sensor helper function ---

 
# Main program 
try:
        
    # This code repeats forever
    while True:

        # Read from the distance sensor
        dist = distance()
            
        print("Measured Distance = {0} cm".format(dist))
                
        # Move the servo
        angle = (int(dist/180) + 1) * 180 - abs((int(dist/180) + 1) * 180 -dist*180/200)
        print(angle)
        pwm_servo.start(set_duty_cycle(angle))
        
        time.sleep(0.5)
 


# Reset by pressing CTRL + C
except KeyboardInterrupt:
        print("Measurement stopped by User")
finally:
        GPIO.cleanup()
