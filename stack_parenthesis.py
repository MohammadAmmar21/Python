###STACK
##TO CHECK BALANCING

a = '())'
stac = []
flag = True
for i in range(len(a)):
    if (a[i] == '(' or a[i] == '[' or a[i] == '{'):
        if(i == len(a) - 1):
            flag = False
        else:
            stac.append(a[i])
    elif (a[i] == ')' or a[i] == '}' or a[i] == ']'):
        if(i == 0 or len(stac) == 0):
            flag = False
            break
        else:
            stac.pop()
print(flag)
if(len(stac) != 0 or flag == False):
    print('not balanced')
else:
    print('bal')
