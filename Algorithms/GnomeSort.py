import time
import random
import numpy as np

def GnomeSort(A,n):
    ind=0
    
    while ind < n:
        if ind == 0: 
            ind = ind+1
        if A[ind] >= A[ind - 1]: 
            ind = ind+1
        else: 
            A[ind],A[ind-1] = A[ind-1],A[ind] 
            ind = ind-1
  
    return A

randArr = np.random.randint(0,1000,1000)
n = len(randArr)

sTime = time.time()
randArr = GnomeSort(randArr, n) 
eTime = time.time()

print(randArr)
print((eTime - sTime), "seconds")
