import sys
sys.path.append('/home/pi/openalpr/src/bindings/python/openalpr')
import logging
from datetime import datetime
from openalpr import Alpr
from picamera import PiCamera
from time import sleep
import cv2
from cv2 import *

# 'gb' means we want to recognise UK plates, many others are available
alpr = Alpr("eu", "/etc/openalpr/openalpr.conf","/usr/share/openalpr/runtime_data/")

from car_color_classifier_yolo3 import car_color_classifier, color_net, COLORS_color, predict_car_color
from car_make_model_classifier_yolo3 import car_make_classifier, make_net, COLORS_make, predict_car_make

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)
now = datetime.now()
logFile = now.strftime("%d_%m_%Y_%H_%M_%S")
output_file_handler = logging.FileHandler(logFile)
stdout_handler = logging.StreamHandler(sys.stdout)

a_logger.addHandler(output_file_handler)
a_logger.addHandler(stdout_handler)

#cap = cv2.VideoCapture(0)   # 0 -> index of camera
#Create a picam object
camera = PiCamera()
#start the camera preview
camera.start_preview()
sleep(2)
try:
    # Let's loop forever:
    while True:

        # Take a photo
        print('Taking a photo')
        camera.capture('/home/pi/Github/ALPR_RPi/make_color/latest.jpg')
        now = datetime.now()
        a_logger.debug(now.strftime("%d %m %Y %H:%M:%S"))
####   if you wish to capture using opencv , uncomment this code
##        if not cap.isOpened():
##            cap = cv2.VideoCapture(0)   # 0 -> index of camera
##            print("Error opening video")
##        while(cap.isOpened()):
##            status, frame = cap.read()
##            if status:
##                 #cv2.imshow('frame', frame)
##                cv2.imwrite('filename.jpg',frame)
##             # do_stuff_with_frame(frame)
##                key = cv2.waitKey(33)
##                break
#####################
        # Ask OpenALPR what it thinks
        print("Running LPR..")
        start = time.time()
        analysis = alpr.recognize_file("/home/pi/Github/ALPR_RPi/make_color/latest.jpg")
        end = time.time()
        # show timing information on ALPR
        print("[INFO] ALPR took {:.6f} seconds".format(end - start))

        # If no results, no car!
        if len(analysis['results']) == 0:
            #a_logger.debug('No number plate detected')
            print('No number plate detected')

        else:
            #cap.release()
            #cv2.destroyAllWindows()
            number_plate = analysis['results'][0]['plate']
            a_logger.debug('Number plate detected: ' + number_plate)
            # call car_color_calssifier_yolo3.py code here
            print("Detecting Color..")
            color_output = predict_car_color(classifier=car_color_classifier,net=color_net, COLORS=COLORS_color, filename='/home/pi/Github/ALPR_RPi/make_color/latest.jpg')
                
            if len(color_output) == 0:
            #a_logger.debug('Color could not be identified')
                print('Color could not be identified')
            else:
                a_logger.debug(color_output)

        
# 
#         # call car_make_model_classifier_yolo3 code here
            print("Detecting Make & Model..")
            make_output = predict_car_make(classifier=car_make_classifier, net=make_net, COLORS=COLORS_make, filename='/home/pi/Github/ALPR_RPi/make_color/latest.jpg')
            if len(make_output) == 0:
            #a_logger.debug('Make could not be identified')
                print('make could not be identified')
            else:
                a_logger.debug(make_output)

except KeyboardInterrupt:
    print('Shutting down')
    #cap.release()
    #cv2.destroyAllWindows()
    camera.stop_preview()
    camera.close()
    alpr.unload()
