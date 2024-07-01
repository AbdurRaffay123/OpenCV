import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

# Load your specific image files
img_files = [
    'card.png',
    'book.png',
    # Add more image paths as needed
]

# Check model file existence
model_path = 'resources/Model/keras_model.h5'
label_path = 'resources/Model/labels.txt'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"The model file '{model_path}' does not exist.")
if not os.path.exists(label_path):
    raise FileNotFoundError(f"The label file '{label_path}' does not exist.")

# Load classifier
classifier = Classifier(model_path, label_path)

# Load images
imgArrow = cv2.imread('resources/arrow.png', cv2.IMREAD_UNCHANGED)
imgWasteList = []
pathFolderWaste = "resources/Waste"
pathList = os.listdir(pathFolderWaste)
for path in pathList:
    imgWasteList.append(cv2.imread(os.path.join(pathFolderWaste, path), cv2.IMREAD_UNCHANGED))

imgBinsList = []
pathFolderBins = "resources/Bins"
pathList = os.listdir(pathFolderBins)
for path in pathList:
    imgBinsList.append(cv2.imread(os.path.join(pathFolderBins, path), cv2.IMREAD_UNCHANGED))

classDic = {0: None, 1: 0, 2: 0, 3: 3, 4: 3, 5: 1, 6: 1, 7: 2, 8: 2}

# Process each image file
for img_path in img_files:
    # Read image
    img = cv2.imread(img_path)

    # Resize image if necessary
    imgResize = cv2.resize(img, (454, 340))
    imgBackground = cv2.imread('resources/background.png')

    prediction = classifier.getPrediction(img)
    classID = prediction[1]
    print(classID)
    if classID != 0:
        imgBackground = cvzone.overlayPNG(imgBackground, imgWasteList[classID - 1], (909, 127))
        imgBackground = cvzone.overlayPNG(imgBackground, imgArrow, (978, 320))
        classIDBin = classDic[classID]

    imgBackground = cvzone.overlayPNG(imgBackground, imgBinsList[classIDBin], (895, 374))
    imgBackground[148:148 + 340, 159:159 + 454] = imgResize

    cv2.imshow("Output", imgBackground)
    cv2.waitKey(0)  # Wait for any key press to show the next image

cv2.destroyAllWindows()