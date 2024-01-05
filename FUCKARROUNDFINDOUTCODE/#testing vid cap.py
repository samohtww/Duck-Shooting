#testing arrowdetection
import numpy as np 
import cv2 
  
cap = cv2.VideoCapture(1) 
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)
  
# initializing subtractor  
object_detector = cv2.bgsegm.createBackgroundSubtractorMOG(history=1000)  
  
while True: 
    ret, frame = cap.read()        
    make_1080p()
    # applying on each frame 
    mask = object_detector.apply(frame)
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL) 
    cv2.namedWindow("Image1", cv2.WINDOW_NORMAL) 
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:

        area = cv2.contourArea(cnt)
        if area < 700 and area > 300:
            cv2.drawContours(frame, [cnt], -1, (255, 0, 0), 4) 


    # Using resizeWindow() 
    cv2.resizeWindow("Image", 1800, 300) 
    cv2.resizeWindow("Image1", 1800, 300) 

    cv2.imshow('Image', mask)
    cv2.imshow('Image1', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows() 