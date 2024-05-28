from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import svgwrite

def load_image(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale
    pixel_array = np.array(image)
    return pixel_array

def apply_fourier_transform(pixel_array):
    f_transform = np.fft.fft2(pixel_array)
    f_transform_shifted = np.fft.fftshift(f_transform)  # Shift zero frequency to center
    return f_transform_shifted

def fourier_epicycles(f_transform, num_vectors):
    t = np.linspace(0, 1, 1000)
    epicycles = np.zeros_like(t, dtype=np.complex128)  # Use np.complex128 for NumPy scalar type
    indices = np.arange(-num_vectors//2, num_vectors//2)
    
    for k in indices:
        coeff = f_transform[k % len(f_transform)]
        freq = 2 * np.pi * k
        epicycles += coeff * np.exp(1j * freq * t)
    
    return t, epicycles


def generate_svg_path(epicycles):
    path_data = "M " + " ".join(f"{np.real(pt)},{np.imag(pt)}" for pt in epicycles)
    return f'<path d="{path_data}" fill="none" stroke="black" />'

def main(image_path, output_path, num_vectors):
    pixel_array = load_image(image_path)
    f_transform_shifted = apply_fourier_transform(pixel_array)
    
    # Take the first row for simplicity
    signal = pixel_array[0]
    f_transform = np.fft.fft(signal)
    
    t, epicycles = fourier_epicycles(f_transform, num_vectors)
    
    # Plot the epicycles
    plt.plot(np.real(epicycles), np.imag(epicycles))
    plt.title('Epicycles')
    plt.show()
    
    # Generate SVG
    svg_path_data = generate_svg_path(epicycles)
    svg_content = f"""
    <svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
        {svg_path_data}
    </svg>
    """
    
    # Save the SVG file
    with open(output_path, "w") as file:
        file.write(svg_content)
    
    print(f"SVG file created: {output_path}")

# Example usage
if __name__ == "__main__":
    image_path =  r'D:\fascinating-math\math\fourier\IMG_1798.JPG'
    output_path = r'D:\fascinating-math\math\fourier\output\epicycles.svg'
    num_vectors = 50
    main(image_path, output_path, num_vectors)
