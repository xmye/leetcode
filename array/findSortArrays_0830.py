import math

def findSortArrays(A,B,k):
    if k == 0:
        return
    m = len(A)
    n = len(B)
    Am,Bj = float("-Inf"),float("-Inf")
    if m > n:
        return findSortArrays(B,A,k)
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

arr1 = [1,2,3,5,8]
arr2 = [0,4,6,7]
print("initial array:\n",arr2)
print("result array:\n",findSortArrays(arr1,arr2,8))

# A,B两个有序数组，找出合并后的第k个数。找出A[i] B[j],使 i+j+1=k
# 已知 i+j个元素，若A[i]>B[j]，则第k个元素为 B[j]。
# 若不满足A[i]>B[j]，说明A数组过小，j>0,第k个元素为B[j],若j<0,说明A[i-1]为第k个元素。

