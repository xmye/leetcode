def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

# O(n^2)

def bubble_sort_update(arr):
    for i in range(len(arr)):
        current_state = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                current_state = True

        if not current_state:
            break

arr = [2,8,7,1,3,5,6,4]
print("initial array:\n",arr)
bubble_sort(arr)
print("result array:\n",arr)
