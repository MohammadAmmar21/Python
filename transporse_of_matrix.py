###transporsepfamatrix
rows,cols=map(int,input().split(" "))
print(rows,cols)
mat1=[]
mat2=[]
for i in range(rows):
    temp=list(map(int,input().split(" ")))
    mat1.append(temp)
print(mat1)
for i in mat1:
    print(" ".join(map(str,i)))
for i in range(rows):
    row=[]
    for j in range(cols):
        temp=mat1[j][i]
        row.append(temp)
    mat2.append(row)
print(mat2)
for i in mat2:
    print(" ".join(map(str,i)))
