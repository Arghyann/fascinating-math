import svgpathtools
import numpy as np

def extract_points_from_svg(svg_file_path, num_points=500):
    # Read the SVG file
    paths, attributes = svgpathtools.svg2paths(svg_file_path)
    
    points = []

    for path in paths:
        # Get points on the path
        for i in range(num_points):
            t = i / num_points
            point = path.point(t)
            points.append(np.complex128(point)/15)

    return points

# Example usage
svg_file_path = r'D:\fascinating-math\math\fourier\epicycles\output\testsvg.svg'
points = extract_points_from_svg(svg_file_path)

