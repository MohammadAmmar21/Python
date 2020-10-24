##linear_search

n=list(map(int,input().split(" ")))
print(n)
i=flag=0
x=30
while(i<len(n)):
    if n[i]==x:
        flag=1
        break
    i=i+1
if(flag==1):
    print(i+1)
else:
    print("nf")
