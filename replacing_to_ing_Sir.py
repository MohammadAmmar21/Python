##replacing ing adding ly


n=input()
print(n)
print(len(n))
b="ing"
j=len(n)
print(j)
if(n[(j-3):] == "ing"):
    print(n+"ly")
else:
    print(n+"ing")
