#!/usr/bin/python3

import cv2
import pyttsx3
import time
import numpy as np

def warning():
    engine = pyttsx3.init()
    engine.say("your motion is detected")
    engine.runAndWait()

def    create_image_diff(x,y,z):
    img1_df = cv2.absdiff(x,y)
    img2_df = cv2.absdiff(y,z)
    img3 = cv2.bitwise_and(img1_df,img2_df)
    return img3


# starting web cam
cap = cv2.VideoCapture(0)
tp1 = cap.read()[1]
tp2 = cap.read()[1]
tp3 = cap.read()[1]

#converting to greyscale
gray1 = cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

blank_img=np.zeros((480,640))
#gray4 = cv2.cvtColor(blank_img,cv2.COLOR_BGR2GRAY)
while True:
    #calling function
    new_img = create_image_diff(gray1,gray2,gray3)
    print (new_img.shape)
    cv2.imshow('wind1',new_img)
    #capture new img
    status,frame = cap.read()
    cv2.imshow('new',frame)
    #exchange img

    a = gray1 = gray2
    b = gray2 = gray3
    c = gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #if new_img == blank_img.all:
    #    warning()
    #    print ("asa")    
        
                                            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyeAllWindows()
cap.release()




    
