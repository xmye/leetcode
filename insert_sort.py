def insert_sort(arr):
    for i in range(1,len(arr)):
        unsort = arr[i]
        j = i-1
        while j>=0 and arr[j] > unsort:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = unsort

arr = [2,8,7,1,3,5,6,4]
print("initial array:\n",arr)
insert_sort(arr)
print("result array:\n",arr)


