Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##hexadecimal_to_binary
>>> import math
n=int(input())
s=0
i=0
while(n>0):
    a=int(n%10)
    s=s+a*(pow(16,i))
    n=n/10
    i+=1
print(int(s))
