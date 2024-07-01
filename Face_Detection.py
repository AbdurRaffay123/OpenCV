import cv2

faceCascade= cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/face1.PNG')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    print("X: ",x, " Y: ",y," W: ",w," H: ",h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(img, "Face", 
                        (x + (w // 2) - 10, y + (h // 2) - 10), 
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255), 1)


cv2.imshow("Result", img)
cv2.waitKey(0)