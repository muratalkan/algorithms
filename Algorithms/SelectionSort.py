import time
import numpy as np

def swap(Arr, x, y):
    Arr[[x,y]] = Arr[[y,x]]
    return Arr
    
def SelectionSort(Arr):
   n = len(Arr)
   for i in range(0, (n-2)+1):
       minInd=i
       for j in range(i+1, (n-1)+1):
           if Arr[j] < Arr[minInd]:
               minInd = j
       Arr = swap(Arr, i, minInd)

randArr=np.random.randint(1,100,1000)

sTime = time.time()
SelectionSort(randArr)
eTime = time.time()

print(randArr)
print("%.10f seconds" %(eTime - sTime))
