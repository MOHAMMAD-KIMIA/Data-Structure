def countingSort(array):
    size=len(array)
    output=[0]*size
    #count array
    count=[0]*10
    #count each number in the main array and put the counting number in count array
    for i in range(0,size):
        count[array[i]]+=1
    #adding 
    for i in range(1,10):
        count[i]+=count[i-1]

    i=size-1
    while i>=0:
        output[count[array[i]]-1]=array[i]
        count[array[i]]-=1
        i-=1

    for i in range(0,size):
        array[i]=output[i]
