import numpy as np

# 找出从第一个元素开始的下降序列，两个指针分别从下降序列和数组尾部扫描，求出最大距离
# 求出 最大 j-i while lst[j]>lst[i] and j > i
def maxIndexDistance(lst):
    if lst == None or len(lst)<2:
        return
    isDescSeq = np.zeros((len(lst)),dtype=bool)
    m = lst[0]
    n = len(lst)
    for i in range(len(lst)):
        if lst[i] < m:
            isDescSeq[i] = True
            m = lst[i]

    i,j = n-1, n-1; maxDist = 0

    while i > 0:
        if isDescSeq[i] == False:
            i -= 1
            continue
        while lst[j] <= lst[i] and j > i:
            j -= 1
        if maxDist < j - i:
            maxDist = j - i
        i -= 1
    return maxDist

lst = [5,3,4,0,1,4,1]
dist = maxIndexDistance(lst)
print('maxIndexDistance is', dist)