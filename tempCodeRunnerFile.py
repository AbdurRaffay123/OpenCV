
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

# Display the original, blurred, Canny edge, and contour images
imgStack = stackImages(0.5