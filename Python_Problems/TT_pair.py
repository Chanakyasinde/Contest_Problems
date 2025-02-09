n=int(input())
s=input()
prefix=[0]*n
if s[0]=="T":
    prefix[0]=1
else:
    prefix[0]=0
for i in range(1,n):
    if s[i]=="T":
        prefix[i]=prefix[i-1]+1
    else:
        prefix[i]=prefix[i-1]

q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    l=l-1
    r=r-1
    ans=prefix[r]-prefix[l-1]
    if l==0:
        print((prefix[r]*(prefix[r]-1))//2)
    else:
        print((ans*(ans-1))//2)
