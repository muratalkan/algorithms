import time
import numpy as np

def InsertionSort(Arr):
    n = len(Arr)
    
    for i in range(1, (n-1)+1):
        k = Arr[i]
        j = i-1
        while j >= 0 and Arr[j] > k:
            Arr[j+1] = Arr[j]
            j = j-1
        Arr[j+1] = k
        

randArr = np.random.randint(1, 100000, 1000)

print("Some part of Initial Array:")
print(randArr[:10])

sTime = time.time()
InsertionSort(randArr)
eTime = time.time()

print("Some part of Sorted Array:")
print(randArr[:10])
     
print((eTime - sTime), "seconds")
