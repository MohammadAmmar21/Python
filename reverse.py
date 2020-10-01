n=list(map(str,input().split(" ")))
print(n)
for i in n:
    tem = list(i)
    a = 0
    b = len(tem)-1
    while(a < b):
        c = tem[a]
        tem[a] = tem[b]
        tem[b] = c
        a += 1
        b -= 1
    print(''.join(tem))
