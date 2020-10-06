##pattern3

n=int(input())
print(n)
v=1
for i in range(n):
    print(" "*(n-i),end=" ")
    print("*"*(v))
    v+=2
