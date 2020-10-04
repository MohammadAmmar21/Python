
##max repeating charachter in a string



n=list(input())
print(n)
dic={}
max=0
for i in n:
    if(not dic.get(i)):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
for j in dic.keys():
    if dic[j]>1:
        print(j)
    if dic[j]>max:
        max=dic[j]
print(max)
for keys,item in dic.items():
    if item==max:
        print(keys)
