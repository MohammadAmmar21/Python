# You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.

# Input Description:
# First line contains a number ‘n’. Then next line contains n space separated numbers.

# Output Description:
# Print the difference of indices of largest and smallest array

# Sample Input :
# 5
# 1 6 4 0 3
# Sample Output :
# -2

n=int(input())
lis=list(map(int,input().split()))
max=lis[0]
min=lis[0]
for i in range(n):
    if lis[i]>max:
        max=lis[i]
        max_i = i
    if lis[i]<min:
        min=lis[i]
        min_i=i
diff=max_i-min_i
print(abs(diff))
