# You are given a paragraph.Your task is to print the words that come just after articles.

# Input Description:
# You are given a string ‘s’

# Output Description:
# print the words that come just after articles and -1 if there are no articles

# Sample Input :
# The sun rises in the east

# Sample Output :
# sun east

s=input()
vowel=["a","e","i","o","u","A","E","I","O","U"]
b=[]
for i in s:
    if i not in vowel:
        b.append(i)
if b:
    print("".join(b))
else:
    print("-1")
    
