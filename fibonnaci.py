##fibonacii
#input:5
##output:5 10 15 25 40
n=int(input())
print(n)
n1=5
n2=10
n3=0
print(n1,n2,end=" ")
for i in range(2,n):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
