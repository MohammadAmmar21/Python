##star_pattern5

n=int(input())
print(n)
v=1
for i in range(n):
    print(" "*(v),end=" ")
    print(" * "*(n-i),end=" ")
    print(" "*(v))
    v+=1
