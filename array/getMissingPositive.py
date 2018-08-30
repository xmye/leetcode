def getMissingPositive(arr):
    n = len(arr)
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] < n:
            if (arr[i] - 1) != i and arr[arr[i]-1] != arr[i]:
                tmp = arr[arr[i]-1]
                arr[arr[i]-1] = arr[i]
                arr[i] = tmp
                i -= 1
    print(arr)
    for i in range(len(arr)):
        if arr[i] - 1 != i and arr[i] <= n:
            return i+1
    return n+1

arr = [5,3,1,2]
print("initial array:\n",arr)
print("result array:\n",getMissingPositive(arr))