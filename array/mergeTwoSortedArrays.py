def mergeTwoSortedArrays(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    arr = [float("-inf")]*(m+n)
    while n > 0:
        if m <= 0 or arr1[m-1] < arr2[n-1]:
            arr[m+n-1] = arr2[n-1]
            n -= 1
        else:
            arr[m+n-1] = arr1[m-1]
            m -= 1
    return arr

arr1 = [1,2,3,5,8]
arr2 = [0,4,6,7]
print("initial array:\n",arr2)
print("result array:\n",mergeTwoSortedArrays(arr1,arr2))