arr = [ 2, 3, 4, 6 , 7, 8, 9, 10, 40 ]
x = 10
low = 0
high = len(arr) - 1
mid = 0
ans = False

while low <= high: 
    mid = (high + low) // 2
    if x > arr[mid]:
        low = mid + 1
    elif x < arr[mid]: 
        high = mid - 1
    else: 
        ans = mid
        break
print(ans)