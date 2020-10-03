##Write a Python program to find the first non-repeating character in given string.
##input:ammartamizh
##output:['a', 'm', 'm', 'a', 'r', 't', 'a', 'm', 'i', 'z', 'h']
##{'a': 3, 'm': 3, 'r': 1, 't': 1, 'i': 1, 'z': 1, 'h': 1}
##r


s=list(input())
print(s)
dic={}
for i in s:
    if(not dic.get(i)):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
for j in dic.keys():
    if dic[j]==1:
        print(j)
        break
    
