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
        z=grid[i][j]                    #iterate over the entire complex plane for all values of z
        for k in range(iterations):
            if(np.abs(z)>2):
                image[i][j]=k
                break
            z = z**2 - 0.75 + 1j*0.1           #edit the function here
plt.figure(figsize=(10,10))

plt.imshow(image, extent=(xcords.min(),xcords.max(),ycords.min(),ycords.max()),cmap='inferno')
plt.colorbar(label='Number of iterations before the point blows up')
        
    
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Julia')
plt.show()