##octal_to_binary
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
num=s
rem=""
while num>=1:
    rem+=str(num%2)
    num=math.floor(num/2)
binary=""
for i in range(len(rem)-1,-1,-1):
    binary=binary +rem[i]
print(binary)
