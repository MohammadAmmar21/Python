##number_pattern5
n=int(input())
v=1
for i in range(n):
    for j in range(i+1):
        print(v,end=" ")
    print("\r")
    v+=2
