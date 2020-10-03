###Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). Go to the editor
###Sample function and result :
###insert_end('Python') -> onononon
###insert_end('Exercises') -> eseseses


n=list(input())
print(n)
j=len(n)-1
if(len(n)>2):
    print("".join((n[j-1],n[j]))*4)
else:
    print("bhag")
