def perm(a,k=0):
    if k== len(a):
        print(a)
    else:
        for i in range(k,len(a)):
            a[i],a[k]=a[k],a[i]
            perm(a,k+1)
            a[k],a[i]=a[i],a[k]
perm([1,2,3])