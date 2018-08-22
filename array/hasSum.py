def hasSum(lst,target):
    if lst == None or len(lst) < 2:
        return
    lst.sort()
    i = 0
    j = len(lst) - 1
    while i != j:
        if lst[i] + lst[j] > target:
            j -= 1
        if lst[i] + lst[j] < target:
            i += 1
        if lst[i] + lst[j] == target:
            return lst[i],lst[j]


def hasSum_On(lst,target):
    if lst == None or len(lst) < 2:
        return
    d = dict()
    for i in range(len(lst)):
        if target - lst[i] in d:
            return lst[i],target - lst[i]
        if lst[i] not in d:
            d[i] = lst[i]


class twoSum():
    num = dict()
    def insert(self,newnum):
        originCount = 0
        if newnum in self.num:
            return self.num.get(newnum)
        else:
            self.num.put(newnum,originCount+1)

    def test(self,target):
        for i in range(len(self.num)):
            if target - lst[i] in self.num:
                isDouble = (target == lst[i] * 2)
                if ~isDouble and self.num.get(lst[i]) == 1:
                    return True
        return False

lst = [2,3,7,8,4,5]
print(hasSum_On(lst,10))
