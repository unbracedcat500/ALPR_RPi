from openalpr import Alpr
#from picamera import PiCamera
from time import sleep
#from SimpleCV import Camera
import cv2
from cv2 import *


# 'gb' means we want to recognise UK plates, many others are available
alpr = Alpr("eu", "/etc/openalpr/openalpr.conf",
            "/usr/share/openalpr/runtime_data")
#camera = PiCamera()

try:
    # Let's loop forever:
    while True:

        # Take a photo
        print('Taking a photo')
        #camera.capture('/home/pi/latest.jpg')
        cap = cv2.VideoCapture(0)   # 0 -> index of camera
        if not cap.isOpened():
                print("Error opening video")
        while(cap.isOpened()):
            status, frame = cap.read()
            if status:
                cv2.imshow('frame', frame)
                cv2.imwrite('filename.jpg',frame)
            # do_stuff_with_frame(frame)
            key = cv2.waitKey(25)
            if key == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break


        #s, img = cam.read()
        #if s:    # frame captured without any errors
        #    cv2.namedWindow("cam-test",cv2.WINDOW_AUTOSIZE)
        #    cv2.imshow("cam-test",img)
        #    cv2.waitKey(0)
        #    cv2.destroyWindow("cam-test")
        #    cv2.imwrite("filename.jpg",img) #save image
        

        # Ask OpenALPR what it thinks
        analysis = alpr.recognize_file("filename.jpg")

        # If no results, no car!
        if len(analysis['results']) == 0:
            print('No number plate detected')


        else:
            number_plate = analysis['results'][0]['plate']
            print('Number plate detected: ' + number_plate)

        #call car_color_calssifier_yolo3.py code here
        #call car_make_model_classifier_yolo3 code here

        # Wait for five seconds
        sleep(20)

except KeyboardInterrupt:
    print('Shutting down')
    cam.release()
    alpr.unload()