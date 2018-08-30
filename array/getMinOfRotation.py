def getMinOfRotation(arr):
    if arr == None or len(arr) == 0:
        return
    left,right = 0,len(arr)-1
    m = arr[left]
    while left < right:
        mid = int((right + left)/2)
        m = min(m,arr[mid])
        if arr[left] == arr[mid] or arr[right] == arr[mid]:
            left += 1
        if arr[left] < arr[mid]:
            left = mid + 1
            m = min(m,arr[left])
        else:
            right = mid - 1
            m = min(m, arr[left]) # m = min(m, arr[mid])
    return m


def searchRotationArray(arr,k):
    left,right = 0,len(arr) - 1
    while left < right:
        mid = int((left + right)/2)
        if arr[mid] == k:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= k and k < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if arr[left] >= arr[mid]:
            if arr[mid] < k and k <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1


arr = [3,4,5,6,1,2]
print("initial array:\n",arr)
print("result array:\n",getMinOfRotation(arr))
print("result array:\n",searchRotationArray(arr,5))
