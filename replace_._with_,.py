###Write a Python program to swap comma and dot in a string. Go to the editor
###Sample string: "32.054,23"
###Expected Output: "32,054.23"
S = input()
k = ""
for i in S:
    if i == ",":
        k = k + "."
        continue
    if i == ".":
        k = k + ","
        continue
    else:
        k = k + i
print(k)
