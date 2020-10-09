##stringswithnumbers1
##aa11bb22cc33dd44
##16

n=input()
print(n)
b=[]
c=[]
for i in n:
    if i.isdigit():
        b.append(i)
print(b)
a=len(b)
print(a)
for i in n:
    if i.isalpha():
        c.append(i)
print(c)
d=len(c)
print(d)
sum=a+d
print(sum)
