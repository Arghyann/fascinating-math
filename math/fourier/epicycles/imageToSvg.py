import cv2
import numpy as np
import xml.etree.ElementTree as ET

# Read the image
image = cv2.imread(r'D:\fascinating-math\math\fourier\epicycles\output\IMG_1798.JPG')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to get a binary image
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)

# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an SVG XML tree
svg_tree = ET.Element('svg', xmlns="http://www.w3.org/2000/svg", version="1.1")

# Iterate over each contour
for contour in contours:
    # Convert contour to SVG format
    path_data = 'M'
    for point in contour.squeeze():
        path_data += f'{point[0]},{point[1]} '
    path_data += 'Z'

    # Create SVG path element
    path_element = ET.Element('path', d=path_data, fill="none", stroke="black", stroke_width="1")

    # Add path element to SVG tree
    svg_tree.append(path_element)

# Create SVG tree object
svg_output = ET.ElementTree(svg_tree)

# Save SVG file
svg_output.write('output_outline.svg')
