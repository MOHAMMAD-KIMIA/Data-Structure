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
