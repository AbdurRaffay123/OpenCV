import cv2

# Set reasonable dimensions for display (not really needed for image processing, but good for display)
frameWidth = 640
frameHeight = 480

# Load the number plate cascade
# Update the path to the Haar cascade file you have downloaded
cascade_path = "haarcascades/haarcascade_russian_plate_number.xml"
nPlateCascade = cv2.CascadeClassifier(cascade_path)

# Ensure the cascade file loaded correctly
if nPlateCascade.empty():
    raise IOError(f"Failed to load the number plate cascade file from path: {cascade_path}")

minArea = 200  # Minimum area of the detected number plate
color = (255, 0, 255)  # Color for the rectangle around the number plate

# Read the image file
image_path = "resources/CarNumberPlate1.png"  # Change this to the path of your image
img = cv2.imread(image_path)

# Check if image is loaded successfully
if img is None:
    raise IOError(f"Failed to load image at path: {image_path}")

# Resize the image to a smaller size for display and detection
imgResized = cv2.resize(img, (frameWidth, frameHeight))

# Convert the image to grayscale
imgGray = cv2.cvtColor(imgResized, cv2.COLOR_BGR2GRAY)

# Adjust detection parameters
numberPlates = nPlateCascade.detectMultiScale(
    imgGray,
    scaleFactor=1.1,  # How much the image size is reduced at each image scale
    minNeighbors=4,   # How many neighbors each rectangle should have to retain it
    minSize=(30, 30),  # Minimum size of detected object
)

imgRoi = None  # Initialize imgRoi to None

# Debugging information
print(f"Number plates detected: {len(numberPlates)}")

for (x, y, w, h) in numberPlates:
    area = w * h
    if area > minArea:
        cv2.rectangle(imgResized, (x, y), (x + w, y + h), color, 2)
        cv2.putText(imgResized, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        imgRoi = imgResized[y:y + h, x:x + w]
        cv2.imshow("ROI", imgRoi)

# Display the result image
cv2.imshow("Result", imgResized)

# Save the result if a number plate is detected
if imgRoi is not None:
    save_path = "resources/Scanned/NoPlate_detected.jpg"
    cv2.imwrite(save_path, imgRoi)
    print(f"Number plate saved at: {save_path}")
else:
    print("No number plate detected to save.")

# Wait for a key press and then close the display windows
cv2.waitKey(0)
cv2.destroyAllWindows()