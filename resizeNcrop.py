import cv2
import numpy as np

# Read the image using OpenCV
img = cv2.imread("resources/road.png")

# Check if the image was successfully read
if img is not None:
    # Print the shape of the image
    print("Image shape:", img.shape)
else:
    print("Error: Image not found or unable to read the image.")
    exit()  # Exit if image not found

# Display the original image using OpenCV's imshow
cv2.imshow("Beautiful Road", img)
cv2.waitKey(0)  # Wait for a key press to close the window

# Resize the image
width, height = 150, 200
img_resized = cv2.resize(img, (width, height))
print("Resized image shape:", img_resized.shape)

# Display the resized image
cv2.imshow("Resized Beautiful Road", img_resized)
cv2.waitKey(0)  # Wait for a key press to close the window

# Crop the image: showing only the road
# Note: BGR to RGB conversion is not needed for OpenCV imshow as it expects BGR format
croppedImg = img[420:631, 0:659]  # Crop the image

# Display the cropped image
cv2.imshow("Cropped Beautiful Road", croppedImg)
cv2.waitKey(0)  # Wait for a key press to close the window

# Resize cropped image to the original shape
Reshape_croppedImg = cv2.resize(croppedImg, (img.shape[1], img.shape[0]))

# Display the reshaped cropped image
cv2.imshow("Cropped Road Full Size", Reshape_croppedImg)
cv2.waitKey(0)  # Wait for a key press to close the window

# Close all OpenCV windows
cv2.destroyAllWindows()