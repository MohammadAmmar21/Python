Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##binary to decimal
>>> num=list(input())
value=0
for i in range(len(num)):
    digit=num.pop()
    if digit=='1':
        value=value+pow(2,i)
print(value)
