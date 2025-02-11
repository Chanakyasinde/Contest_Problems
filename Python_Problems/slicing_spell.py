# Your code here
list1=list(map(int, input().split()))
start, end=map(int, input().split())
final_list=list1[start:end:2]
print(final_list)
