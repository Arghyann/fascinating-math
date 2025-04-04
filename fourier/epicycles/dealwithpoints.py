import numpy as np

def read_points_from_file(file_path, image_height):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize lists for points
    points = []
    x_coords = []
    y_coords = []

    # First pass - collect all coordinates
    for line in lines:
        x, y = map(int, line.strip().split(','))
        x_coords.append(x)
        y_coords.append(y)
    
    # Calculate scaling factor based on max dimensions
    max_coord = max(max(x_coords), max(y_coords))
    target_size = 800  # Similar to test1.txt range
    scale_factor = target_size / max_coord if max_coord > target_size else 1
    
    # Second pass - create scaled points
    for x, y in zip(x_coords, y_coords):
        scaled_x = x * scale_factor
        scaled_y = (image_height - y) * scale_factor  # Flip and scale y
        points.append(np.complex128(complex(scaled_x, scaled_y)))

    return points