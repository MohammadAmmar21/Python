#     You are given a string.Your task is to print only the consonants present in the string without affecting the sentence spacings if present. If no consonants are present print -1

# Input Description:
# You are given a string ‘s’.

# Output Description:
# Print only consonants.

# Sample Input :
# I am shrey 
# Sample Output :
#  m shry
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
    
