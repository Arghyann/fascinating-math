import random
import numpy as np
import matplotlib.pyplot as plt
def simulateGoodReview(probability=0.93,numberOfevents=100):
    array=[]
    for i in range(numberOfevents):
        if random.random()<=probability:
            array.append(True)
        else:
            array.append(False)

    return array

def arrangeData(dataArray):
    for i in range(10):
        x=simulateGoodReview()
        count=0
        for j in range(len(x)):
            if(x[j]):
                count+=1
        dataArray[count]+=1

array=np.zeros(101)
arrangeData(array)
plt.bar(array,np.arange(len(array)))
plt.title('Bar Graph with Indices as Labels')
plt.xlabel('Index')
plt.ylabel('Values')

# Display the graph
plt.show()