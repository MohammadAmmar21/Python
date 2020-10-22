
##strong number
import math
n=int(input())
fact=1
s=0
while(n>0):
    a=int(n%10)
    for i in range(1,a+1):
        fact=fact*i
    s=s+fact
    n=math.floor(n/10)
    fact=1
print(s)
