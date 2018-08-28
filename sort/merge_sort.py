def merge(left,right):
    arr = []
    i,j = 0,0
    while i< len(left) and j< len(right):
        if left[i] > right[j]:
            arr.append(right[j])
            j += 1
        else:
            arr.append(left[i])
            i+=1
        if j == len(right):
            for k in left[i:]:
                arr.append(k)
        if i == len(left):
            for k in right[j:]:
                arr.append(k)
    return arr

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) / 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left,right)


arr = [2, 8, 7, 1, 3, 5, 6, 4]
print("initial array:\n", arr)
merge_sort(arr)
print("result array:\n", merge_sort(arr))