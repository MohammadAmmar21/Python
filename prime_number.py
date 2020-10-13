##prime no

num1=int(input())
print(num1)
if num1>1:
    for i in range(2,num1):
        if(num1%i==0):
            print("not a prime")
            break
    else:
        print("prime")
else:
    print("not prime")
