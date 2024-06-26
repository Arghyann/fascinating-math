#generate a simple black and white mandelbrot set
import numpy as np
import matplotlib.pyplot as plt
iterations=100
resolution=1000

image = np.full((resolution, resolution), iterations)
xcords=np.linspace(-2,2,resolution)
ycords=np.linspace(-2,2,resolution)
x,y=np.meshgrid(xcords,ycords)
grid=x+1j*y
for i in range(resolution):
    for j in range(resolution):
        z=0
        for k in range(iterations):
            if(np.abs(z)>2):
                image[i][j]=k
                break
            z = z**2 + grid[i][j]              #edit the function here
plt.figure(figsize=(10,10))

plt.imshow(image, extent=(xcords.min(),xcords.max(),ycords.min(),ycords.max()))
plt.colorbar(label="number of iterations before blowing up")       
        
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Mandelbrot')
plt.show()