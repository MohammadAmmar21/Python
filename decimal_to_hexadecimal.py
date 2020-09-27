import math
n=int(input())
rem=""
while n>=1:
    rem+=str(n%16)
    n=math.floor(n/16)
binary=""
for i in range(len(rem)-1,-1,-1):
    binary=binary+rem[i]
print(binary)
    
