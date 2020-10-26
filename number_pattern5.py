##nopattern_6
n=int(input())
print(n)
for i in range(n):
    for j in range(n-i+1):
        print(j,end=" ")
    print("\r")
