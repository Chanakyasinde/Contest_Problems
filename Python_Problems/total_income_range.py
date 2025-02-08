# prefix sum technic

n=int(input())
lst=list(map(int, input().split()))
prefix=[0]*n
for i in range(n):
    if i==0:
        prefix[i]=lst[i]
    else:
        prefix[i]=lst[i]+prefix[i-1]
q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    if l==0:
        print(prefix[r])
    else:
        print(prefix[r]-prefix[l-1])
