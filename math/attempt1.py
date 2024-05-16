#give it some time to compute. It iterates over 250000 pixels, one by one, over a lot of iterations

import numpy as np
import matplotlib.pyplot as plt
import random


class fractal:
    def __init__(self):
        self.rootsArray = []
        self.colour = []

    def f(self, z):                                  #original function
        function = (z**6) -1           
        self.rootsArray = np.roots([1,0,0,0,0,0,-1])  #takes in the polnomial as an array of coefficients
        for i in range(len(self.rootsArray)):    #change it if you also change the function
            red = random.uniform(0, 1)
            blue = random.uniform(0, 1)
            green = random.uniform(0, 1)
            self.colour.append([red, green, blue])
        return function
        
    def fDer(self,z):
        return 6*(z**5)                  #and here to change the function(derivative of the function)


    def assignColour(self,imag):
        distances = [abs(root - imag) for root in self.rootsArray]  # Calculate distances to each root
        min_distance_index = distances.index(min(distances))  # Find the index of the closest root
        return self.colour[min_distance_index]  # Return the color corresponding to the closest root

    def newtonMethod(self,imag,iterations=10):
        for i in range(iterations):
            imag=imag-(self.f(imag)/self.fDer(imag))
        return imag



class ComplexPlaneClass:
    def __init__(self,x,y) -> None:
        self.resolution=500
        self.xcords=np.linspace(x,y,self.resolution)  
        self.ycords=np.linspace(x,y,self.resolution)  
        x,y=np.meshgrid(self.xcords,self.ycords)
        self.complexGrid=x+1j*y
    
    def generateNewtonFractal(self):
        newtonFractal=fractal()
        ComplexValues=np.zeros((self.resolution,self.resolution,3),dtype=float)
        for i in range(self.resolution):
            for j in range(self.resolution):
                point=self.complexGrid[i,j]
                approximation=newtonFractal.newtonMethod(point)
                colour=newtonFractal.assignColour(approximation)
                ComplexValues[i][j]=colour
        return ComplexValues

    def plotPoints(self,values):
        plt.figure(figsize=(10,10))

        plt.imshow(values, extent=(self.xcords.min(), self.xcords.max(), self.ycords.min(), self.ycords.max()))
        
        # Set labels and title
        plt.xlabel('Real')
        plt.ylabel('Imaginary')
        plt.title('Newton Fractal')
        
        # Show the plot
        
        plt.show()




complexP=ComplexPlaneClass(-2,2)
complexP.plotPoints(complexP.generateNewtonFractal())

        

