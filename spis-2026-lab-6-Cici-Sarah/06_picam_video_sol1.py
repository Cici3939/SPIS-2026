# This program illustrates how to capture frames in a video stream and how to do further processing on them
# It uses numpy to do the calculations and OpenCV to display the frames

# General libraries
import time
import numpy as np 
# Libraries to control the camera
from picamera2 import Picamera2
import cv2



# Initialize the camera
camera = Picamera2()

# Configure the camera
config = camera.create_video_configuration(
    #-----------------------------------------------------
    # Picam natively uses RGB, but OpenCV, which we use for manipulating
    # and displaying images, uses BGR. So we will work with BGR.
    # We can change the settings of picam to give us BGR instead, and
    # we don't need to do an explicit conversion. Confusingly, "RGB888"
    # means that frames will be grabbed BGR format (and vice versa).
    #-----------------------------------------------------
    main = {"size": (640, 480), "format": "RGB888"},
    controls={"FrameRate": 32},
)
camera.configure(config)


# Main program 
try:

    # Start the camera
    camera.start()
    print("To end the program, press q when hovering over a window")
    print("or press CTRL+C in the terminal.")
    
    # Continuously grab camera frames
    while True:

        # Grab a frame
        img = camera.capture_array()
        
        #-----------------------------------------------------
        # We will use numpy to do all our image manipulations
        #-----------------------------------------------------

        # Get the size of the np array
        # numpy orders axes as (height, width, channels) -- rows first, then columns
        h,w,d = img.shape
        
        # Make a copy of the image
        img1 = img.copy()

        # Modify the copy of the image 
        img1[h//4:3*h//4 , w//4:3*w//4 , :] = 255 - img1[h//4:3*h//4 , w//4:3*w//4 , :]
        
        img2 = img.copy()
        start_pix_x = 0
        start_pix_y = 0
        end_pix_x = 0
        end_pix_y = 0
        start_found = False
        for x in range(w):
            for y in range(h):
                if img2[y][x][0] >= 200 and img2[y][x][1] >= 200 and img2[y][x][2] >= 200:
                    if not start_found:
                        start_pix_x = x
                        start_pix_y = y
                        start_found = True
                    else:
                        end_pix_x = x
                        end_pix_y = y
        print(start_pix_x,start_pix_y)
        print(end_pix_x,end_pix_y)
        img2[start_pix_y:end_pix_y, start_pix_x, :] = 255 - img2[start_pix_y:end_pix_y, start_pix_x, :]
        img2[start_pix_y:end_pix_y, end_pix_x, :] = 255 - img2[start_pix_y:end_pix_y, end_pix_x, :]
        img2[start_pix_y, start_pix_x:end_pix_x, :] = 255 - img2[start_pix_y, start_pix_x:end_pix_x, :]
        img2[end_pix_y, start_pix_x:end_pix_x, :] = 255 - img2[end_pix_y, start_pix_x:end_pix_x, :]
        
        # Show the frames (OpenCV assumes BGR color representation)
        cv2.imshow("Original frame", img)
        #cv2.imshow("Modified frame", img1)
        cv2.imshow("Modified frame2", img2)
        
        # The waitKey command is needed to force openCV to show the image
        # It looks for a keystroke for x ms (with x the argument) and otherwise continues
        # In this case, the program check if the user pressed 'q'
        if cv2.waitKey(1) == ord('q'):
            break


# Reset by pressing CTRL + C
except KeyboardInterrupt:
        print("Program stopped by User")
finally:
    # Clean up the resources
    cv2.destroyAllWindows()
    camera.stop()
    camera.close()
        
