import time
import random

def QuickSort(Arr, start, end):
    if start <= end:
        s = Partition(Arr, start, end)
        QuickSort(Arr, start, s-1)
        QuickSort(Arr, s+1, end)
        
def Partition(Arr, start, end):
    piv = Arr[start]
    i = start+1
    j = end
    flag = True
    
    while flag:
        while i <= j and Arr[i] <= piv:
            i = i+1
        while j >= i and Arr[j] >= piv:
            j = j-1
        if i >= j:
            flag = False
        else:
           Arr[i],Arr[j] = Arr[j],Arr[i]

    if piv > Arr[j]:
        Arr[start],Arr[j] = Arr[j],Arr[start]

    return j

randList = []
for i in range(0,1000):
    randList.append(random.randrange(0,1000000))

sTime = time.time()
QuickSort(randList, 0, len(randList)-1)
eTime = time.time()

print(randList)
print((eTime - sTime), "seconds")
