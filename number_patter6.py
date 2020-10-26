##numberpattern6
n=int(input())
a=1
for i in range(n):
    for j in range(1,i+2):
        print(a,end=" ")
    print("\r")
    a+=1
    
