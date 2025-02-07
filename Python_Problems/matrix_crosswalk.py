n=int(input())
l=[]
mid=n//2
result=0
for i in range(n):
    s = list(map(int,input().split()))
    l.append(s)
for i in range(n):
    result+=l[i][mid]
    result+=l[mid][i]
result-=l[mid][mid]
print(result)
