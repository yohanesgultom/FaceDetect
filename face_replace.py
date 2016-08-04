import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
replacementPath = sys.argv[2]
cascPath = sys.argv[3]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageReplacement = cv2.imread(replacementPath, -1)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    y = y - h / 1.5
    x = x - w / 1.5
    h *= 2
    w *= 2
    imageReplacementResized = cv2.resize(imageReplacement, (w, h))
    for c in range(0, 3):
        image[y:y+h, x:x+w, c] = imageReplacementResized[:, :, c] * (imageReplacementResized[:, :, 3]/255.0) + image[y:y+h, x:x+w, c] * (1.0 - imageReplacementResized[:, :, 3]/255.0)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
