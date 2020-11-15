import time

def SequentialSearch(Arr, x):
   n = len(Arr)
   i = 0
   
   while i < n and Arr[i] != x:
       i = i+1
   if i < n:
       return i
   else:
       return -1

List = [1, 2, 32, 8, 17, 19, 42, 13, 0]

print(List)
val = int(input("Enter a value from list: "))

sTime = time.time()
ind = SequentialSearch(List, val)
eTime = time.time()

if ind == -1:
    print("\nNot Found!")
else:
    print("\nIndex of the given element is:", ind)

print((eTime - sTime), "seconds")

