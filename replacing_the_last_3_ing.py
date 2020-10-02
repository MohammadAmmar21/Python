### Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

n=input()
print(n)
print(len(n))
b="ing"
j=len(n)-1
print(j)
if(n.endswith("ing")):
    print(n+"ly")
else:
    print(n+"ing")
