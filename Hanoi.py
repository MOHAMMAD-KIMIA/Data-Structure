i = int(input("number of disks: "))
def hanoi(disk=1,start='a',temp='b',end='c'):
    if disk==1:
        print(start + " go to " + end)
    else:
        hanoi(disk-1,start,end,temp)
        print(start + " go to " + end)
        hanoi(disk-1,temp,start,end)
hanoi(i,'a','b','c') 