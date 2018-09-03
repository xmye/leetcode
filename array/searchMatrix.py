def searchMatrix(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    low = 0
    high = m*n - 1
    while low < high:
        mid = (low + high)/2
        if target == matrix[mid/n][mid%n]:
            return True
        if target <  matrix[mid/n][mid%n]:
            high = mid - 1
        if target >  matrix[mid/n][mid%n]:
            low = mid + 1
    return False

def searchRange(lst,target):
    range = [-1,-1]
    low = 0
    upper = len(lst)
    if lst[upper-1] < target:
        return range
    while low < upper:
        mid = int((low + upper)/2)
        if lst[mid] < target:
            low = mid + 1
        else:
            upper = mid
    if lst[low] != target:
        return range
    else:
        range[0] = low
    upper = len(lst)
    while low < upper:
        mid = int((low + upper)/2)
        if lst[mid] > target:
            upper = mid
        else:
            low = mid + 1
    range[1] = upper - 1
    return range

arr = [1,3,4,4,5]
print(searchRange(arr,4))