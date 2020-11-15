import time
import numpy as np

def swap(Arr, x, y):
    Arr[[x, y]] = Arr[[y, x]]
    return Arr
    
def BubbleSort(Arr):
   n = len(Arr)
   for i in range(0, (n-2)+1):
       for j in range(0, (n-2-i)+1):
           if Arr[j+1] < Arr[j]:
               Arr = swap(Arr, j, j+1) 

randArr = np.random.randint(1, 100, 1000)

sTime = time.time()
BubbleSort(randArr)
eTime = time.time()

print(randArr)
print((eTime - sTime), "seconds")
