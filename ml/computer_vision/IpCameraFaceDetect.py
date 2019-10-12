url = "https://192.168.43.1:8080/shot.jpg"
import requests
import cv2
import numpy

findFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    data = requests.get(url, verify = False)
    image = data.content
    imageArray = bytearray(image)
    imageID = numpy.array(imageArray)
    img = cv2.imdecode(imageID, -1)
    face_coord = findFace.detectMultiScale(img)
    
    #To Handle Loss of Face Coordinate
    if face_coord is ():
        pass
    else:
        x = face_coord[0][0]
        y = face_coord[0][1]
        w = face_coord[0][2]
        h = face_coord[0][0]
        rectPhoto = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 5)	
        cv2.imshow('Live Video', img)
        if cv2.waitKey(1) == 13:
            break

cv2.destroyAllWindows()
