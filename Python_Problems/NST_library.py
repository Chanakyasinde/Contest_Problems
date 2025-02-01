N = int(input())
t = int(input())
m = int(input())
rate = 0
if N<=0:
    print("Invalid rental duration")
else:
    if 1<=N<=3:
        rate+=N*1
    elif 4<=N<=7:
        rate+=N*0.75
    elif N>=8:
        rate+=N*0.5
    if t==1:
        rate+=2
    elif t==2:
        rate-=rate*0.1
    elif t==3:
        rate=rate
    if m==1:
        rate-=rate*0.1
    elif m==2:
        rate=rate
    print(int(rate))
