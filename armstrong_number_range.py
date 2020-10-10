##armstrongnumberforagivenrange

n1=int(input())
n2=int(input())
for i in range(n1,n2):
    sum=0
    temp=i
    while(temp>0):
        digit=temp%10
        sum+=digit**3
        temp//=10
        if(sum==i):
            print(i)
    
