###Write a Python program to change a given string to a new string where the first and last chars have been exchanged

n=list(input())
print(n)
i=0
j=len(n)-1
print(j)
while(i<j):
    c=n[i]
    n[i]=n[j]
    n[j]=c
    i+=1
    j-=1
    break
print(" ".join(n))
