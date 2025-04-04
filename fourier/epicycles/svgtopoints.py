import svgpathtools
import numpy as np

def extract_points_from_svg(svg_file_path, num_points=500):
    # Read the SVG file
    paths, attributes = svgpathtools.svg2paths(svg_file_path)
    
    # First pass - find bounds
    x_coords = []
    y_coords = []
    
    for path in paths:
        for i in range(num_points):
            t = i / num_points
            point = path.point(t)
            x_coords.append(np.real(point))
            y_coords.append(np.imag(point))
    
    # Calculate scaling factor
    max_coord = max(max(abs(min(x_coords)), abs(max(x_coords))), 
                    abs(min(y_coords)), abs(max(y_coords)))
    target_size = 800  # Similar to test1.txt range
    scale_factor = target_size / max_coord if max_coord > target_size else 1

    # Second pass - create scaled points
    points = []
    for path in paths:
        for i in range(num_points):
            t = i / num_points
            point = path.point(t)
            x = np.real(point) * scale_factor
            y = -np.imag(point) * scale_factor  # Flip y
            points.append(np.complex128(complex(x, y)))

    return points