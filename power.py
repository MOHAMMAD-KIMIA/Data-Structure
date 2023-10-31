def power(n,m):
    if m==0:
        return 1
    else:
        return n*power(n,m-1)


a=int(input("number:"))
b=int(input(f"power:"))
print(pow(a,b))