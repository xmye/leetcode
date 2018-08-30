def findKthSortArrays(A,B,k):
    if k == 0:
        return
    m = len(A)
    n = len(B)
    Am,Bj = float("-Inf"),float("-Inf")
    if m > n:
        return findKthSortArrays(B,A,k)
    left = 0
    right = m
    while left < right:
        mid = int(left + (right - left)/2)
        j = abs(k-1-mid)
        if j >= n or A[mid] < B[j]:
            left = mid + 1
        else:
            right = mid
    if left - 1 >= 0:
        Am = A[left-1]
    if k-1-left >= 0:
        Bj = B[k-1-left]
    return max(Am,Bj)

def findKthSortArraysII(A,B,k):
    if k == 0:
        return
    m = len(A)
    n = len(B)
    Am,Bj = float("-Inf"),float("-Inf")
    Ai, Bj1 = float('inf'), float('inf')
    if m > n:
        return findKthSortArraysII(B,A,k)
    left = 0
    right = m
    while left < right:
        mid = int(left + (right - left)/2)
        j = int(abs(k-1-mid))
        if j >= n or A[mid] < B[j]:
            left = mid + 1
        else:
            right = mid
    if left - 1 >= 0:
        Am = A[left-1]
    if k-1-left >= 0:
        Bj = B[k-1-left]
    valK = max(Am,Bj)
    if ((n+m)/2 == 1):
        return valK
    if k - left < n:
        Bj1 = B[k-left]
    if left < m:
        Ai = A[left]
    return float((valK + min(Bj1,Ai))/2)

def findMedianSortedArray(arr1,arr2):
    if (arr1 == None or len(arr1) == 0) and (arr2 == None or len(arr2) == 0):
        return
    m = len(arr1)
    n = len(arr2)
    k = int((n+m-1)/2 +1)
    return findKthSortArraysII(arr1,arr2,k)

arr1 = [1,2,3,5,8]
arr2 = [0,4,6,7]
print("initial array:\n",arr2)
print("result array:\n",findKthSortArrays(arr1,arr2,8))
print("result array:\n",findMedianSortedArray(arr1,arr2))


# A,B两个有序数组，找出合并后的第k个数。找出A[i] B[j],使 i+j+1=k
# 已知 i+j个元素，若A[i]>B[j]，则第k个元素为 B[j]。
# 若不满足A[i]>B[j]，说明A 数组过小，j>0,第k个元素为B[j],若j<0,说明A[i-1]为第k个元素。

