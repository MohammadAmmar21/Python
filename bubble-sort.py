lis = [1,65,2,12,4,5,3]
n = len(lis)
for i in range(n):
    for j in range(n-i-1):
        if lis[j] > lis[j+1]:
            lis[j], lis[j+1] = lis[j+1], lis[j]
print(lis)
