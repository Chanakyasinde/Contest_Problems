def count_balanced_subarrays(N, K, arr, a, b):
    count_a = 0
    count_b = 0
    balanced_count = 0

    # Initialize first window
    for i in range(K):
        if arr[i] == a:
            count_a += 1
        if arr[i] == b:
            count_b += 1
    
    # Check if first window is balanced
    if count_a == count_b and count_a > 0:
        balanced_count += 1

    # Slide the window
    for i in range(K, N):
        # Remove outgoing element
        if arr[i - K] == a:
            count_a -= 1
        if arr[i - K] == b:
            count_b -= 1

        # Add incoming element
        if arr[i] == a:
            count_a += 1
        if arr[i] == b:
            count_b += 1

        # Check if window is balanced
        if count_a == count_b and count_a > 0:
            balanced_count += 1

    return balanced_count

# Input handling
N, K = map(int, input().split())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

# Function call and output
print(count_balanced_subarrays(N, K, arr, a, b))
