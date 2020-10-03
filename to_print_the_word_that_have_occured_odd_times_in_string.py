###to print the odd words repeated odd times in a string
##input:saamuel
##output:smue

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
    if(dic[j]%2!=0):
        print((j),end=" ")
