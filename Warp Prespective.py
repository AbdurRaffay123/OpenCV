import numpy as np
import cv2

# Load the image
CardImg = cv2.imread("resources/card.jpg")

# Check if the image was loaded successfully
if CardImg is None:
    raise FileNotFoundError("The image file could not be found. Please check the file path.")

# Image size for transformation
width, height = 250, 350

# Points from the original image
pts1 = np.float32([[326, 125], [446, 207], [213, 305], [326, 379]])

# Points for the destination image
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Compute the perspective transform matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation
imgOutput = cv2.warpPerspective(CardImg, matrix, (width, height))

# Draw circles on the original image at the points of interest
for x in range(4):
    cv2.circle(CardImg, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 0, 255), cv2.FILLED)

# Display the original image with points
cv2.imshow("Original Image with Points", CardImg)

# Display the transformed image
cv2.imshow("Transformed Image", imgOutput)

# Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()