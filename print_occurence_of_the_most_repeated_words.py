### Write a Python program to count repeated characters in a string. Go to the editor
##Sample string: 'thequickbrownfoxjumpsoverthelazydog'
##Expected output :
##o 4
##e 3
##u 2
##h 2
###r 2
##t 2###

s=(input())
print(s)
dic={}
for i in s:
    if(not dic.get(i)):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
for j in dic.keys():
    if dic[j]>1:
        print(j,end=" ")
        print(dic[j])
