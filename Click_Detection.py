import cv2
import os

# Define the image path
image_path = cv2.imread("C:\Users\Abdur Raffay Khan\OPENCV\resources\book.png")

# Check if the file exists at the specified path
if not os.path.isfile(image_path):
    print(f"Error: File not found at {image_path}")
else:
    # Read the image
    img = cv2.imread(image_path)

    # Check if the image was successfully read
    if img is None:
        print("Error: Could not read the image.")
    else:
        # Display the image
        cv2.imshow("Image", img)

        # Wait for a key press to close the image window
        cv2.waitKey(0)

        # Close all OpenCV windows
        cv2.destroyAllWindows()
