 #~#Write a Python program to find ###the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

 n=input()
print(n)
if(n.find('not')and n.find('poor')):
    a=n.replace('not that poor','good')
print(a)
