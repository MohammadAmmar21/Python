# You are provided with an array in which all elements are repeated thrice except one which is repeated twice.Your task is to print that number.

 

# O(n) time and O(1) extra space

# Input Description:
# First line contains a number denoting size of array ‘n’.Next line contains n space separated numbers

# Output Description:
# Print the number which is repeated twice

# Sample Input :
# 5
# 13 12 13 12 13
# Sample Output :
# 12

n=int(input())
lis=list(map(int,input().split(" ")))
dic={}
for i in lis:
    if(not dic.get(i)):
        dic[i] = 1
    else:
        dic[i] += 1
for j in dic.keys():
    if(dic[j] == 2):
        print(j)
        break
