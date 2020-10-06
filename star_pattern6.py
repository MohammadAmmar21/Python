#star_pattern6


n=int(input())
print(n)
for i in range(n):
    print("*"*(i+1))
for j in range(n):
    print("*"*(n-j-1))
