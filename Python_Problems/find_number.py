def find(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return find(n-1)+(3*find(n-2))
