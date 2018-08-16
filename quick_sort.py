def quickSort(arr,first,last):
    if first < last:
        div = partition(arr,first,last)
        quickSort(arr,first,div)
        quickSort(arr,div+1,last)
    else:
        return

def partition(arr,first,last):
    i = first - 1
    for j in range(first,last):
        if arr[j] <= arr[last]:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[last] = arr[last],arr[i+1]

    return i

arr = [2,8,7,1,3,5,6,4]
print("initial array:\n",arr)
quickSort(arr,0,len(arr)-1)
print("result array:\n",arr)