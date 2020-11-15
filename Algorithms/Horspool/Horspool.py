def ShiftTable(P):
    pLen = len(P)

    S = [pLen] * 256
    for i in range(pLen-1):
        S[ord(P[i])] = pLen-i-1
    return S

def Horspool(T, P):
    tLen = len(T)
    pLen = len(P)

    S = ShiftTable(P)
    i = pLen - 1

    while i <= tLen-1:
        k = 0
        while k <= pLen-1 and P[pLen-1-k] == T[i-k]:
            k = k+1
        if k == pLen:
            return i - pLen+1
        else:
            i=i+S[ord(T[i])]
    return -1

file = open("impact.txt", "r+")
List = file.read()
print("File content is:")
print("\n"+ List)

Str = input("\nEnter a string to search: ")
out = Horspool(List, Str)
print(out)
