# This program demonstrates a more flexible way to implement a delay

# Import the relevant libraries
import time

# Specify how long we want to wait (in seconds)
delayTarget = 1


# Keep track of the time
# NOTE: initialise to the current time, not 0. Starting at 0 makes the first
# comparison run against the Unix epoch, so the first line printed is ~1.8e9 seconds.
LastTime = time.time()

# Main program 
try:
        
    # This code repeats forever
    while True:
        
        # Check the current time
        currentTime = time.time()

        # Check if we have waited long enough
        if (currentTime - LastTime > delayTarget):
            print("Amount of time that has passed: {0}".format(currentTime-LastTime))
            angle = 0
            pwm_servo.start(set_duty_cycle(angle))
            print ("Moving to angle 0")
                           
            angle = 180
            pwm_servo.start(set_duty_cycle(angle))
            print ("Moving to angle 180")
            LastTime = currentTime
           

            
# Reset by pressing CTRL + C
except KeyboardInterrupt:
        print("Program stopped by User")
finally:
        pass
