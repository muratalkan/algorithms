def HeapBottomUp(H):
    n = len(H) - 1

    for i in range(n//2, 0, -1):
        k = i
        v = H[k]
        heap = False

        while not heap and k*2 <= n:
            j = 2*k
            if j < n:
                if H[j] < H[j+1]:
                    j = j+1
            if v >= H[j]:
                heap = True
            else:
                H[k] = H[j]
                k = j
        H[k] = v
    return H

HA = [0,2,9,7,6,5,8,10]
print("Beginning Array: ", HA)
print("Array, After Heapify: ", HeapBottomUp(HA))

n = len(HA)-1
print("Root Node: ", HA[1])
i=2
j=2

while (i <= n):
    print("%d. Level Nodes:" %j)
    print(HA[i:i*2])
    i *= 2
    j += 1
