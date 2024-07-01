import cv2
import numpy as np

# Create a blank image
img = np.zeros((512, 512, 3), np.uint8)

print(img.shape)

# Draw a green line from the top-left to the bottom-right
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)

# Display the image with the line
cv2.imshow("Line", img)
cv2.waitKey(0)  # Wait for a key press to proceed

# Draw a red rectangle from (350, 100) to (450, 200)
cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)

# Display the image with the rectangle
cv2.imshow("Rectangle", img)
cv2.waitKey(0)  # Wait for a key press to proceed

# Draw a blue circle with center at (150, 400) and radius 50
cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)

# Display the image with the circle
cv2.imshow("Circle", img)
cv2.waitKey(0)  # Wait for a key press to proceed

# Add green text "Draw Shape" at (75, 50)
cv2.putText(img, "Draw Shape", org=(100, 110),color=(0, 150, 0),fontFace=4, fontScale=2,thickness=2)

# Display the image with the text
cv2.imshow("Text", img)
cv2.waitKey(0)  # Wait for a key press to proceed

# Draw a blue ellipse centered at (200, 200) with axes (100, 50) rotated by 30 degrees
cv2.ellipse(img, (200, 200), (100, 50), 30, 0, 360, (255, 0, 0), 3)

# Display the image with the ellipse
cv2.imshow("Ellipse", img)
cv2.waitKey(0)  # Wait for a key press to proceed

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()