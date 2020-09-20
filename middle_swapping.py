
# Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).
# Sample Testcase :
# INPUT
# hello
# OUTPUT
# he*lo



aq = list(input().strip())
leng = len(aq)
isEven = leng%2 == 0
if(isEven):
    middle = int(len(aq)/2)
    before = middle-1
    aq[middle]="*"
    aq[before]="*"
else:
    middle = int(len(aq)/2)
    aq[middle]="*"

print("".join(aq))
