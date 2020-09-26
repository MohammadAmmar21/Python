# Assume you are a student studying in school.You are given a task to find first negative integer for each and every window of size k.

# Input Description:
# First line contains an integer n denoting the size of the array. The next line contains n space separated integers forming the array. The last line contains the window size k.

# Output Description:
# Print the first negative integer in that window.If all the numbers are positive print 0

# Sample Input :
# 7
# 1 -2 -3 -4 5 6 -7
# 3
# Sample Output :
# -2 -2 -3 -4 -7

n=int(input())
lis=list(map(int,input().strip().split(" ")))
k=int(input())
neg = []
for i in range(n-k):
    for j in lis[i:i+3]:
        if(j < 0):
            neg.append(j)
            break
print(' '.join(map(str, neg)))
