import cv2
import numpy as np
import svgwrite

# Load the image
img0 = cv2.imread(r'D:\fascinating-math\math\fourier\epicycles\output\QNNl8I01.svg')

# Convert to grayscale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# Resize the image
resized = cv2.resize(gray, (190, 190))

# Apply blur
blurred = cv2.GaussianBlur(resized, (5, 5), 0)  # Adjusted kernel size to (5, 5)

# Binarize the image
_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Delete small components
nb_components, output, stats, _ = cv2.connectedComponentsWithStats(binary, connectivity=8)
sizes = stats[:, -1]
mask_sizes = sizes > 50
mask_sizes[0] = 0
binary_cleaned = np.zeros(output.shape)
for i in range(1, nb_components):
    if mask_sizes[i]:
        binary_cleaned[output == i] = 255

# Extract contours
contours, _ = cv2.findContours(binary_cleaned.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
pts = np.vstack(contours).squeeze()

# Center points
center = np.mean(pts, axis=0)
pts_centered = pts - center

# Create SVG file
svg_file = 'output.svg'
dwg = svgwrite.Drawing(svg_file, profile='tiny')

# Define a group for the points
points_group = dwg.add(dwg.g(id='points'))

# Add points to the group
for x, y in pts_centered:
    points_group.add(dwg.circle(center=(x, y), r=0.5, fill='black'))

# Save SVG file
dwg.save()
