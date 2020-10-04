##factorial
##in:5
##output:120

n=int(input())
print(n)
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
