def getClosestBigger(arr1,arr2):
    arr1.sort()
    flag = [0] * len(arr1)
    res = []
    for j in range(len(arr2)):
        i = 0
        while i < len(arr1) and (arr1[i] < arr2[j] or flag[i] == 1):
            i += 1
        res.append(arr1[i])
        flag[i] = 1
        # if i == len(arr1) - 1:
        #     break
        if arr1[i] > arr2[j]:
            for i in range(len(arr1)):
                if flag[i] == 0:
                    res.append(arr1[i])
            break
    return res

arr1 = [1,2,3,5]
arr2 = [2,4,1,0]
print("initial array:\n",arr2)
print("result array:\n",getClosestBigger(arr1,arr2))

