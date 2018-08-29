import random

def numInrange(arr,minnum,maxnum):
    arr.sort()
    canran = random.randint(minnum,maxnum)
    while findNum(arr,canran,0,len(arr)-1):
        canran = random.randint(minnum, maxnum)
    return canran


def findNum(arr,key,start,end):
    mid = int((start + end) / 2)
    if start > end or len(arr) == 0:
        return False
    if arr[mid] == key:
        return True
    if arr[mid] < key:
        return findNum(arr,key,mid+1,end)
    if arr[mid] > key:
        return findNum(arr,key,start,mid-1)


arr1 = [1,2,3,5]
print("initial array:\n",findNum(arr1,1,0,len(arr1)-1))
print("result array:\n",numInrange(arr1,1,5))