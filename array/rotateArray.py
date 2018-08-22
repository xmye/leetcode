# array reverse
def rotateArray(lst,k):

    if lst == None or k > len(lst):
        return
    firlst = reverse(lst)
    seclst = reverse(firlst[:k])
    thilst = reverse(firlst[k:])

    return seclst + thilst

def reverse(lst):
    st = 0
    end = len(lst) - 1
    while st < end:
        lst[st],lst[end] = lst[end],lst[st]
        st += 1
        end -= 1
    return lst

arr = [2,8,7,1,3,5,6,4]
print("initial array:\n",arr)
print("result array:\n",rotateArray(arr,2))