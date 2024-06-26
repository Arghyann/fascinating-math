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
            x, y = np.real(point), -np.imag(point)  
            points.append(np.complex128(complex(x, y))/2)

    return points


#svg_file_path = r'D:\fascinating-math\math\fourier\epicycles\output\testsvg.svg'
#points = extract_points_from_svg(svg_file_path)

