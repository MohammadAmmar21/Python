"""Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""
n,k=list(map(str,input().split(" ")))
print(n,k)
s1=n.replace(n[0],k[0])
s2=k.replace(k[0],n[0])
print(s1,end=" ")
print(s2)
