##Write a Python program to find the first repeated character in a given string.
##input:allaballakalla
##output:a


n=list(input())
print(n)
dic={}
for i in n:
    if(not dic.get(i)):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
for j in dic.keys():
    if dic[j]>1:
        print(j)
    break
