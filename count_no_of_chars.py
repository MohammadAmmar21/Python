##Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
#3#Sample String : google.com'
##Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

n=list(input())
print(n)
dic={}
for i in n:
    if not dic. get(i):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
