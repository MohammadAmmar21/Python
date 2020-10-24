##selection sort
a=list(map(int,input().split(" ")))
print(a)
for i in range(len(a)):
    min_=i
    for j in range(i+1,len(a)):
        if a[min_]>a[j]:
            min_=j
    a[i], a[min_] = a[min_], a[i]
for i in range(len(a)):
   print(a[i])
