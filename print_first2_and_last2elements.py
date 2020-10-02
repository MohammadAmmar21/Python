##Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
##Sample String : 'w3resource'
n=list(input())
print(n)
i=0
j=len(n)-1
for i in range(len(n)):
    if len(n)<2:
        print("empty string")
        break
for i in range(len(n)):
    if(len(n)>2):
        print(n[i],n[i+1])
        break
for i in range(len(n)):
    if(len(n)>2):
        print(n[j-1],n[j])
        break
