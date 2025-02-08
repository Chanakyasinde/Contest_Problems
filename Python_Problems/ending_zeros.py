n=int(input())
arr=list(map(int, input().split()))
lst=[]
for item in arr:
    if item!=0:
        lst.append(item)



# for it in arr:
#     if it==0:
#         lst.append(it)
b = n-len(lst)
lst.extend([0]*b)
print(*lst)

# for num in lst:
#     print(num, end=" ")
