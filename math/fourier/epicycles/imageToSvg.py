import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img0 = cv2.imread(r'D:\fascinating-math\math\fourier\epicycles\output\IMG_1798.JPG')

# Convert to grayscale and resize
img_gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
img_resized = cv2.resize(img_gray, (190, 190))

# Binarize the image
_, img_binary = cv2.threshold(img_resized, 15, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Extract contour points
pts = []
for contour in contours:
    pts.extend(contour.squeeze())

# Convert points to NumPy array
pts = np.array(pts)

# Plot the points
plt.plot(pts[:, 0], pts[:, 1], '.')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
