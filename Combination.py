def combination(s, c):
    if c == 0 or c == s:
        return 1
    else:
        return combination(s-1, c) + combination(s-1, c-1)

n = int(input("enter total number of objects in the set: "))
r = int(input("number of choosing objects from the set: "))

print("result:",combination(n, r))