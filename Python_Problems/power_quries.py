def power(ans1, ans2, mod):
    result = 1
    ans1 = ans1 % mod
    while ans2 > 0:
        if ans2 % 2 == 1:
            result = (result * ans1) % mod
        ans1 = (ans1 * ans1) % mod
        ans2 //= 2
    return result

n, q = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * n
mod = (10**9) + 7

prefix[0] = arr[0] % mod
for i in range(1, n):
    prefix[i] = (prefix[i-1] + arr[i]) % mod

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    l1 -= 1
    r1 -= 1
    l2 -= 1
    r2 -= 1
    if l1 > 0 :
        ans1 = (prefix[r1] - prefix[l1-1]) % mod 
    else:
        ans1 = prefix[r1] % mod
    if l2 > 0 :
        ans2 = (prefix[r2] - prefix[l2-1]) % mod 
    else:
        prefix[r2] % mod

    ans = power(ans1, ans2, mod)
    print(ans)
