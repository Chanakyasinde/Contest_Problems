# by using prefix sum technique
n,q=map(int,input().split())
s=input()
m=26
matrix = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if ord(s[j])-97==i:
            matrix[i][j]=matrix[i][j-1]+1
        else:
            matrix[i][j]=matrix[i][j-1]

for i in range(q):
    l,r,c=map(str,input().split())
    l=int(l)
    r=int(r)
    if l==0:
        print(matrix[ord(c)-97][r])
    else:
        print(matrix[ord(c)-97][r]-matrix[ord(c)-97][l-1])
