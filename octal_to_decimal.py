##octal-decimal

import math
n=int(input())
s=0
i=0
while(n>0):
    a=int(n%10)
    s=s+a*(pow(8,i))
    n=n/10
    i+=1
print(int(s))
