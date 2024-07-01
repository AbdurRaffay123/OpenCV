import cv2
import numpy as np

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
        hor_con = [imageBlank] * rows
        for x in range(rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

# Define a 5x5 kernel of ones with unsigned integer type
kernel = np.ones((5, 5), np.uint8)
print(kernel)

# Read the image
img = cv2.imread("resources/Capture.PNG")

# Check if the image was successfully read
if img is None:
    print("The image file could not be found. Please check the file path.")

# Convert the image from BGR to RGB (for display purposes in OpenCV, this step is not necessary)
# However, OpenCV imshow displays BGR by default, so we convert back to BGR for consistent color display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Gaussian Blur with a kernel size of 15x15
img_blur = cv2.GaussianBlur(img, (15, 15), 0)  # No need to convert to RGB again

# Apply Canny edge detection
img_canny = cv2.Canny(img_blur, 100, 100)  # Adjust thresholds as needed

# Perform dilation on the Canny edge image
img_dilation = cv2.dilate(img_canny, kernel, iterations=2)

# Perform erosion on the dilated image
img_eroded = cv2.erode(img_dilation, kernel, iterations=1)

# Display the original, blurred, Canny edge, dilated, and eroded images using OpenCV's imshow
imgStack = stackImages(0.8, ([img, img_rgb, img_blur], 
                             [img_canny, img_dilation, img_eroded]))

cv2.imshow("Stack", imgStack)
cv2.waitKey(0)
# Close all OpenCV windows
cv2.destroyAllWindows()