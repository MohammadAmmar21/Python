##matrix_mul
rows,cols=map(int,input().split(" "))
print(rows,cols)
mat1=[]
mat2=[]
mat3=[]
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
    row = []
    for j in range(cols):
        tem = mat1[i][j]*mat2[i][j]
        row.append(tem)
    mat3.append(row)
print(mat3)
for i in mat3:
    print(" ".join(map(str,i)))
