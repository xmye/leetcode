# import numpy as np

def checkPairable(arr,k):
    if k == 0:
        return
    count = [0]*len(arr)
    for i in arr:
        count[i % k] += 1
    if count[0] % 2 != 0:
        return False
    if k % 2 == 0:
        if (count[int(k/2)] % 2 != 0):
            return False
    for i in range(1,int(k/2)):
        if count[i] != count[k-i]:
            return False
    return True

arr = [2,8,7,1,3,5,6,4]
print("initial array:\n",arr)
print("result array:\n",checkPairable(arr,6))