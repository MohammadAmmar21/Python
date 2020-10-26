##real_Armstrong_number
import math
n1=int(input())
print(n1)
sum=0
temp=n1
while(n1>0):
    digit=int(n1%10)
    sum+=digit**3
    n1=math.floor(n1/10)
print(sum)
if temp==sum:
    print("a")
else:
    print("na")
