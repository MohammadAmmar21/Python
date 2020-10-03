##usage of right split
##input:k,n,o,w,l,e,d,g,e
##expected output:['k,n,o,w,l,e,d,g', 'e']
##'k,n,o,w,l,e,d', 'g', 'e']
##['k,n,o,w,l,e', 'd', 'g', 'e']


s=input()
print(s.rsplit(",",1))
print(s.rsplit(",",2))
print(s.rsplit(",",3))
