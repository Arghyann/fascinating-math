import random
import numpy as np
import matplotlib.pyplot as plt
def simulateGoodReview(probability=0.1,numberOfevents=100):
    array=[]
    for i in range(numberOfevents):
        if random.random()<=probability:
            array.append(True)
        else:
            array.append(False)

    return array

def arrangeData(dataArray):
    for i in range(100000):
        x=simulateGoodReview()
        count=0
        for j in range(len(x)):
            if(x[j]):
                count+=1
        dataArray[count]+=1

array=np.zeros(101)
arrangeData(array)
plt.bar(np.arange(101),array)
plt.title('Binomial distribution')
plt.xlabel('Index')
plt.ylabel('Values')


plt.show()