##star_pattern3

n=int(input())
print(n)
for i in range(n):
    print(" "*(n-i-1),end=" ")
    print("*"*(i+1))
