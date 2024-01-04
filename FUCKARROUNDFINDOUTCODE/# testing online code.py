# testing online code

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 2560)
    cap.set(4, 1440)

while(1):
    _, frame = cap.read()

    # make_1080p()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])


    cv2.namedWindow("frame", cv2.WINDOW_NORMAL) 
    cv2.namedWindow("mask", cv2.WINDOW_NORMAL) 
    cv2.namedWindow("res", cv2.WINDOW_NORMAL)  

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.resizeWindow("frame", 1920, 1080) 
    cv2.resizeWindow("mask", 1920, 1080) 
    cv2.resizeWindow("res", 1920, 1080) 

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()