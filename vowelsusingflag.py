# Given a string S, print 'yes' if it has a vowel in it else print 'no'.
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# yes

s=(input())
print(s)
vowels=["a","e","i","o","u"]
flag=1
for i in s:
    if i in vowels:
        flag=1
        break
if(flag==1):
    print("yes")
else:
    print("no")
