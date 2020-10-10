##number_patterncomplex

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(pow(5,j),end=" ")
    print("\r")
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(pow(5,j),end=" ")
    print("\r")
