##horglass star pattern

n=int(input())
print(n)
v=1
b=1
for i in range(n):
    print(" "*(v),end=" ")
    print(" * "*(n-i))
    v+=1
for j in range(n):
    print(" "*(n-j),end=" ")
    print(" * "*(b))
    b+=1
 
