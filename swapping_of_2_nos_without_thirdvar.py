##program to swap two words without using 3rd variable
s1="good"
s2="morning"
print("before sorting",s1,s2)
s1=s1+s2
s2=s1[0:(len(s1)-len(s2))]
s1=s1[len(s2):]
print(s1,s2)
