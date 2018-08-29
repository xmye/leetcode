

def getTopK(arr,start,end,k):
    div = partition(arr,start,end)
    while k-1 != div:
        if k-1 > div:
            div = partition(arr,div+1,end)
        if k-1 < div:
            div = partition(arr,start,div)
    if k-1 == div:
        return arr[:k]


def partition(arr,start,end):
    i = start - 1
    for j in range(start,end):
        if arr[j] <= arr[end]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i


arr = [2,8,7,1,3,5,6,4]
print("initial array:\n",arr)
l = getTopK(arr,0,len(arr)-1,2)
print("result array:\n",l)