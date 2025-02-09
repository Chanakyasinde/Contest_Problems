n = int(input()) 
heights = list(map(int, input().split()))  

max_jump = 0
max_right = heights[-1]  
for i in range(n - 2, -1, -1):
    if max_right > heights[i]:  
        max_jump = max(max_jump, max_right - heights[i])  
    max_right = max(max_right, heights[i])  

print(max_jump)
