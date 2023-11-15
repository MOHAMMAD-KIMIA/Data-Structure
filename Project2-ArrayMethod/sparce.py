def Sparce(list,n):
    c=0
    for i in range(n):
        for j in range(n):
            if list[i][j]!=0:
                c+=1
    m=[[0 for i in range(3)] for j in range[c+1] ]
    m[0]=[n,n,c]
    x=1
    for i in range(n):
        for j in range(n):
            if list[i][j]!=0:
                m[x][0]=i
                m[x][1]=j
                m[x][2]=list[i][j]
                x+=1
    return m

