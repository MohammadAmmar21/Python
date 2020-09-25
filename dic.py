Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #     You are given an array of ids of prisoners. The jail authority found that there are some prisoners of same id. Your task is to help the authority in finding the common ids.

# Input Description:
# First line contains a number ‘n’ representing no of prisoners. Next line contains n space separated numbers.

# Output Description:
# Print the ids which are not unique. Print -1 if all ids are unique
>>> 
>>> n = int(input().strip())
s = list(map(int, input().split()))
dic = {}
flag = False
for i in s:
    if(not dic.get(i)):
        dic[i] = 'yes'
    else:
        flag = True
        value = i
if(flag == True):
    print(value)
else:
    print('-1')
