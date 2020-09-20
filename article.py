# You are given a paragraph.Your task is to print the words that come just after articles.

# Input Description:
# You are given a string ‘s’

# Output Description:
# print the words that come just after articles and -1 if there are no articles

# Sample Input :
# The sun rises in the east

# Sample Output :
# sun east

s=list(input().split(" "))
print(s)
articles=["the","a"]
b=[]
for i in range(len(s)):
    if s[i] in articles:
        b.append(s[i+1])
if b:
    print(b)
else:
    print(-1)
