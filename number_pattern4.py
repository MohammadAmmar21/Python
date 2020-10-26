##number_pattern4

n=int(input())
print(n)
a=5
for i in range(n):
    for j in range(n-i):
        print(a,end=" ")
    print("\r")
    a-=1
