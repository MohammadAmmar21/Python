##Write a Python program to count and display the vowels of a given text.
##input=ameeru

#Ammar code

# s = input()
# print(s)
# vowels=["a","e","i","o","u"]
# b=[]
# dic={}
# for i in s:
#     if i in vowels:
#         b.append(i)
# for i in b:
#     if(not dic.get(i)):
#         dic[i]=1
#     else:
#         dic[i]+=1
# print((dic))


s = 'qwqwqarei'
vowels=["a","e","i","o","u"]
dic={}
for i in s:
    if i in vowels:
        if(not dic.get(i)):
            dic[i]=1
        else:
            dic[i]+=1
for i in dic.items():
    print(i,j)
