n=int(input())
lst=list(map(int, input().split()))
count=1
maxi=lst[0]
for i in range(n):
    if lst[i]>maxi:
        count+=1
        maxi=lst[i]
print(count)
