##real armstrong no

n1=int(input())
sum=0
temp=n1
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
if(sum==n1):
    print("armstrong")
else:
    print("not armstrong")
