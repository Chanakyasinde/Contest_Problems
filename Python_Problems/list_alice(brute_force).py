n=int(input())
lst=list(map(int, input().split())) 
q=int(input())
for _ in range(q):
    l,r=map(int, input().split())
    count=0
    for i in range(l,r+1):
        if lst[i]%5==0:
            count+=1
    print(count)
