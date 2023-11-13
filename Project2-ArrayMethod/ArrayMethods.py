def findfunc(inp, arr):
    c=0
    for i in range(0, len(arr)):
        if inp == arr[i]:
            print("index:",i)
            c += 1
    if c == 0:
        print("not found")

def delete_element(arr, n, x):
    i = 0
    while i < n:
        if arr[i] == x:
            break
        i += 1

    if i < n:
        n -= 1
        for j in range(i, n):
            arr[j] = arr[j+1]
    
    return n

def insertX(n, arr, x, pos):

    newarr = [0] * (n + 1)
    for i in range(n + 1):
        if i < pos - 1:
            newarr[i] = arr[i]
        elif i == pos - 1:
            newarr[i] = x
        else:
            newarr[i] = arr[i - 1]
    return newarr
