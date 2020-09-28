##addition_of_diagonal_in_matrices
rows,cols=map(int,input().split(" "))
print(rows,cols)
mat1=[]
mat2=[]
mat3=[]
mat4=[]
for i in range(rows):
    temp=list(map(int,input().split(" ")))
    mat1.append(temp)
print(mat1)
for i in mat1:
    print(" ".join(map(str,i)))
rows2,cols2=map(int,input().split(" "))
print(rows2,cols2)
for i in range(cols):
    temp=list(map(int,input().split(" ")))
    mat2.append(temp)
print(mat2)
for i in(mat2):
    print(" ".join(map(str,i)))

##for i in range(rows):
for i in range(rows):
    temp=mat1[i][i]
    mat3.append(temp)
    a=sum(mat3)
print(a)
for i in range(rows):
    temp=mat2[i][i]
    mat4.append(temp)
    b=sum(mat4)
print(b)
print(a+b)
