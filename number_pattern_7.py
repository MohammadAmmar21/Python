##number_pattern7
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(pow(2,i),end=" ")
    print("\r")
