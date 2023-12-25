def merge(arr,l,m,r):
    a=m-l+1
    b=r-m
    lefts=[0]*a
    rights=[0]*b
    for i in range(0,a):
        lefts[i]=arr[l+i]
    for j in range(0,b):
        rights[j]=arr[m+1+j]
    i=0
    j=0
    k=l
    while i<a and j<b:
        if lefts[i]<=rights[j]:
            arr[k]=lefts[i]
            i+=1
        else:
            arr[k]=rights[j]
            j+=1
        k+=1
    while i<a:
        arr[k]=lefts[i]
        i+=1
        k+=1

    while j<b:
        arr[k]=rights[j]
        j+=1
        k+=1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
