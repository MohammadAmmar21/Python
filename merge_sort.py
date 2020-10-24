##mergesort
def mergesort(n):
    print(n)
    if(len(n)>1):
        middle=int(len(n)/2)
        lh=n[:middle]
        rh=n[middle:]
        mergesort(lh)
        mergesort(rh)
        i=j=k=0
        while(i<len(lh) and j<len(rh)):
            if lh[i]<rh[j]:
                n[k]=lh[i]
                i+=1
            else:
                n[k]=rh[j]
                j+=1
            k+=1
        while i<len(lh):
            n[k]=lh[i]
            i+=1
            k+=1
        while j<len(rh):
            n[k]=rh[j]
            j+=1
            k+=1
    print(n)
n=list(map(int,input().split(" ")))
mergesort(n)
print(n)
    
