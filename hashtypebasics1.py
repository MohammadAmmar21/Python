##heshtpe 1

s = input().strip()
k=(input())
print(s)
print(k)
dic={}
for i in s:
    if(not dic.get(i)):
        dic[i]=1
        print('0')
    else:
        dic[i]+=1
        print(dic[i]-1)
