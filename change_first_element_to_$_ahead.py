##Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
##Sample String : 'restart'
##Expected Result : 'resta$t'
s=input()
str1 = s[0]
print(str1)
str2 = s[1:]
print(str2)
str3 = str2.replace(s[0], '$')
print(str3)
str4 = str1+str3
print(str4)
