import random
import time

def Heapify(Arr, n, i):
    largest = i
    x = 2 * i+1
    y = 2 * i+2

    if x < n and Arr[i] < Arr[x]:
        largest = x
    if y < n and Arr[largest] < Arr[y]:
        largest = y
    if largest != i:
        Arr[i],Arr[largest] = Arr[largest],Arr[i]
        Heapify(Arr, n, largest)

def HeapSort(Arr):
    n = len(Arr)

    for i in range(n//2, -1, -1):
        Heapify(Arr, n, i)
        
    print("\nSome part of Heapified Array:", Arr[1:12])

    for i in range(n-1, 0, -1):
        Arr[i],Arr[0] = Arr[0],Arr[i]
        Heapify(Arr, i, 0)

Arr=[]
for i in range(0, 1000):
    Arr.append(random.randrange(0, 1000000))

print("\nSome part of Initial Array:", Arr[1:12])

sTime = time.time()
HeapSort(Arr)
eTime = time.time()

print("\nSome part of Sorted Array:", Arr[1:12])
print("\n", (eTime - sTime), "seconds")
