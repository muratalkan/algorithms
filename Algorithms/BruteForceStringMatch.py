import time

def BruteForceStringMatch(T, P):
   n = len(T)
   m = len(P)
   
   for i in range(0, (n-m)+1):
       j=0
       while j < m and P[j] == T[i+j]:
           j = j+1
       if j == m:
           return i
   return -1
       
Text = "NOBODY_NOTICED_HIM"
Pattern = "NOT"

sTime = time.time()
ind = BruteForceStringMatch(Text, Pattern)
eTime = time.time()

print("Text:", Text)
print("Pattern:", Pattern)
print("\nFirst index of %s in the text is %d" %(Pattern, ind)) 
print((eTime - sTime), "seconds")
