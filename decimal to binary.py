Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##decimal to binary
>>> import math
  
num=int(input())
print(num%2)
rem=""
while num>=1:
    rem+=str(num%2)
    num=math.floor(num/2)
binary=""
for i in range(len(rem)-1,-1,-1):
    binary = binary + rem[i]
     
print(binary)
