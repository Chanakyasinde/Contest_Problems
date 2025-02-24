s=input()
s=s.lower()
count=0
for cha in s:
    if cha == "a":
        count+=1
    else:
        count+=0

print(count)
