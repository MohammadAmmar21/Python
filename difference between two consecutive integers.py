# You are given with an circular array .Your task is calculate the difference between two consecutive number. And if difference is greater than ‘k’, print 1 else print 0

# Input Description:
# You are given two numbers ‘n’, ’m’. Next line contains n space separated integers.

# Output Description:
# Print 1 if the difference is greater than ‘m’.

# Sample Input :
# 5 15
# 50 65 85 98 35
# Sample Output :
# 0 1 0 1 0

n,k=(map(int,input().split()))
lis=list(map(int,input().split()))
for i in range(0,len(lis)-1):
    diff=abs(lis[i]-lis[i+1])
    if diff>k:
        print("1",end="")
    else:
        print("0",end="")
    
