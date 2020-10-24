##swap two numbers without using a 3rdvar
x=int(input())
y=int(input())
print(x,y)
print("before swap",x,y)
x=x+y
y=x-y
x=x-y
print(x,y)
