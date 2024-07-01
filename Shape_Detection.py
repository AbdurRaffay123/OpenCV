import cv2
import numpy as np
import math

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        for x in range(rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        if imgArray[0].shape[:2] == imgArray[1].shape[:2]:
            imgArray = [cv2.resize(img, (0, 0), None, scale, scale) if img.shape[:2] == imgArray[0].shape[:2]
                        else cv2.resize(img, (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
                        for img in imgArray]
        imgArray = [cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) if len(img.shape) == 2 else img for img in imgArray]
        hor = np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    global imgContour
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = w / float(h)

            objectType = "None"
            if objCor == 3:
                objectType = "Triangle"
            elif objCor == 4:
                if 0.95 <= aspectRatio <= 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor == 5:
                objectType = "Pentagon"
            elif objCor == 6:
                objectType = "Hexagon"
            elif objCor > 6:
                if is_circle(cnt):
                    objectType = "Circle"
            
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, 
                        (x + (w // 2) - 10, y + (h // 2) - 10), 
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)

def is_circle(cnt):
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    if perimeter == 0:
        return False
    circularity = 4 * math.pi * (area / (perimeter * perimeter))
    return 0.7 <= circularity <= 1.2

img = cv2.imread("resources/shapes.PNG")

if img is None:
    print("Error: Unable to load image.")
    exit()

imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

# Display the original, blurred, Canny edge, and contour images
imgStack = stackImages(0.8, ([img, imgGray, imgBlur], 
                             [imgCanny, imgContour, imgContour]))

cv2.imshow("Stack", imgStack)
cv2.waitKey(0)
cv2.destroyAllWindows()