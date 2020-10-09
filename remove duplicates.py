# You are a passport issuer, but due to some problems in the system, there are redundant  passport numbers. Your task is to delete all the duplicate passport numbers. You are given a list of passport numbers.

# Input Description:
# You are given length of list.Second line,You are given with a list.

# Output Description:
# Print the list of passport numbers without duplicates.

# Sample Input :
# 5
# A23 B56 B56 C79 D16
# Sample Output :
# A23 B56 C79 D16
n=(input())
lis=list(input().split(" "))
dic={}
Ans = []
for i in lis:
    if(not dic.get(i)):
        dic[i]='yes'
        Ans.append(i)
print(Ans)

lis = [1,65,2,12,4,5,3]
n = len(lis)
for i in range(n):
    for j in range(n-i-1):
        if lis[j] > lis[j+1]: 
            lis[j], lis[j+1] = lis[j+1], lis[j]
print(lis)