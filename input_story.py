# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
# Sample Testcase :
# INPUT
# 4 2
# 1 2 3 3
# OUTPUT
# yes

n,k=input().split()
lis=list(input().split(" "))
if k in lis:
    print("yes")
else:
    print("no")
