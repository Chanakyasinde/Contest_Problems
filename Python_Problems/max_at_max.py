def count_valid_subarrays(arr, x):
    n = len(arr)
    count = 0
    start = 0
    
    for end in range(n):
        if arr[end] > x:
            start = end + 1
        else:
            count += (end - start + 1)
    
    return count

n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = count_valid_subarrays(arr, x)
print(result)
