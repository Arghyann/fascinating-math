import numpy as np

def read_points_from_file(file_path, image_height):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize an empty list to store the points
    points = []

    # Iterate over each line
    for line in lines:
        # Split the line by comma to get x and y coordinates
        x, y = map(int, line.strip().split(','))
        
        # Subtract y from the image height to flip vertically
        flipped_y = image_height - y
        
        # Append the flipped point
        points.append(np.complex128(complex(x, flipped_y)))

    return points
