# Your code here
n=int(input())
s=input()
a=0
b=0
for i in range(n):
    if s[i]=="a":
        a+=1
    else:
        b+=1
if a>b:
    print("Yes")
else:
    print("No")
