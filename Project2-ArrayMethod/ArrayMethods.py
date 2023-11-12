def findfunc(inp, arr):
    c=0
    for i in range(0, len(arr)):
        if inp == arr[i]:
            print("index:",i)
            c += 1
    if c == 0:
        print("not found")
