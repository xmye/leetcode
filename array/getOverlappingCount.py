class interval:

    def __init__(self,lst):
        self.start = lst[0]
        self.end = lst[1]


class point:
    val = 0
    ty = 0
    def __init__(self,val,ty):
        self.val = val
        self.type = ty

def quick_point(lst,first,last):
    if first < last:
        div = parition(lst,first,last)
        quick_point(lst,first,div)
        quick_point(lst,div+1,last)
    else:
        return

def parition(lst,first,last):
    i = first - 1
    for j in range(first,last):
        if lst[j].start <= lst[last].start:
            i += 1
            lst[i],lst[j] = lst[j],lst[i]
    lst[i+1],lst[last] = lst[last],lst[i+1]
    return i

def getOverlappingCount(A):
    m,count = 0,0
    points = []
    if A == None or len(A) == 0:
        return
    for i in range(len(A)):
        points.append(point(A[i].start,0))
        points.append(point(A[i].end,1))
    quick_point(points,0,len(points) - 1)
    for i in range(len(points)):
        print(points[i].val)
        if points[i].type == 0:
            count += 1
            m = max(m,count)
        else:
            count -= 1
    return m

def mergeInterval(A):
    res = []
    if A == None or len(A) == 0:
        return
    quick_point(A,0,len(A) - 1)
    res.append(A[0])
    for i in range(1,len(A)):
        if res[len(res)-1].end >= A[i].start:
            res[len(res)-1].end = A[i].end
            if res[len(res)-1].start > A[i].start:
                res[len(res)-1].start = A[i].start
        else:
            res.append(A[i])
    return res


A0 = interval([1,11])
A1 = interval([10,15])
A2 = interval([0,10])
A3 = interval([20,30])

A = [A0,A1,A2,A3]
# print("result array:\n",getOverlappingCount(A))
res = mergeInterval(A)
for i in range(len(res)):
    print(res[i].start,res[i].end)