def heap_sort(lst):
    #max heap
    def sift_down(start,end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child < end and lst[child] < lst[child + 1]: # find the max child
                child = child + 1
            if lst[child] > lst[root]:
                lst[child],lst[root] = lst[root],lst[child] # exchange child and root
                root = child
            else:
                break

    #creat the maximum heap
    for start in xrange(len(lst)-1//2,-1,-1):
        sift_down(start,len(lst)-1)

    # heap sort
    for end in xrange(len(lst)-1,0,-1):
        lst[0],lst[end] = lst[end],lst[0]
        sift_down(0,end-1)
    return lst

arr = [2, 8, 7, 1, 3, 5, 6, 4]
print("initial array:\n", arr)
heap_sort(arr)
print("result array:\n", arr)