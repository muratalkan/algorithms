import time
import numpy as np
import random
import math

def MergeSort(Arr):
    n = len(Arr)

    if(n > 1):
        m = n//2
        B = Arr[:m]
        C = Arr[m:]

        MergeSort(B)
        MergeSort(C)
        Merge(Arr, B, C)

    return Arr

def Merge(Arr, B, C):
    i=0
    j=0
    k=0

    while(i < len(B) and j < len(C)):
        if(B[i] < C[j]):
            Arr[k] = B[i]
            i = i+1
        else:
            Arr[k] = C[j]
            j = j+1
        k = k+1
    while(i < len(B)):
        Arr[k] = B[i]
        k = k+1
        i = i+1
    while(j < len(C)):
        Arr[k] = C[j]
        k = k+1
        j = j+1

randList = np.random.randint(1,1000,10000)

sTime = time.time()
MergeSort(randList)
eTime = time.time()

print(randList)
print((eTime - sTime), "seconds")
