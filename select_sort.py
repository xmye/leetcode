def select_sort(arr):
    for i in range(len(arr)):
        m = arr[i]
        for j in range(i,len(arr)):
            if arr[j] < m:
                m,arr[j] = arr[j],m
        arr[i] = m

arr = [2,8,7,1,3,5,6,4]
print("initial array:\n",arr)
select_sort(arr)
print("result array:\n",arr)