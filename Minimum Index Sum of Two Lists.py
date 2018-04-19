class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        s1 = set(list1)
        s2 = set(list2)
        s = s1 & s2
        l = list(s)
        output,count = [],[]
        c1,c2,c3 = 0,0,0
        for item in l:
            c1 = int(list1.index(item))
            c2 = int(list2.index(item))
            c3 = c1 + c2
            count.append(c3)
        mcount = min(count)
        for i in range(len(count)):
            if count[i] == mcount:
                output.append(l[i])
        return output
