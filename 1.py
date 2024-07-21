def search(matrix, target):
    if not matrix:
        return False
    
    n = len(matrix)
    m = len(matrix[0])
    
    left = 0 
    right = n * m - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = int(matrix[mid // m][mid % m])
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

data = input().split()
n = int(data[0])
m = int(data[1])

matrix = []
for i in range(n):
    matrix.append(input().split())

target = int(input())

result = search(matrix, target)
print(result)