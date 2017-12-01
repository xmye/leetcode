class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        i = 0
        if right > 10 and left < 10:
            j = left
            while j <= 9:
                result.append(j)
                j += 1
            index = 11
            result += self.getResult(index,right)
            
        if right > 10 and left > 10:
            result = self.getResult(left,right)
                
        if right < 10:
            j = left
            while j <= right:
                result.append(j)
                j += 1
            return result
        return result   
        
    def getResult(self,index,right): 
        result = []
        while index <= right:
            flag = True
            if index % 10 == 0:
                index += 1
                continue
            digit = self.countDigit(index)
            if 0 in digit:
                index += 1
                flag = False
                continue
            accu = 1
            i = 0
            while i < len(digit) :
                if index % digit[i] != 0:
                    flag = False
                    break
                i += 1
            if flag:
                result.append(index)
            index += 1
        return result
            
    def countDigit(self,index):
        digit = []
        if index > 10000:
            digit.append(int(index / 10000))
            index = index % 10000
            if index < 1000:
                digit.append(0)
            if index < 100:
                digit.append(0)
            if index < 10:
                digit.append(0)
        if index > 1000:
            digit.append(int(index / 1000))
            index = index % 1000
            if index < 100:
                digit.append(0)
            if index < 10:
                digit.append(0)
        if index > 100:
            digit.append(int(index / 100))
            index = index % 100
            if index < 10:
                digit.append(0)
        if index > 10:
            digit.append(int(index / 10))
            index = index % 10
        if index > 1:
            digit.append(index)
        return digit

            
            
        
            
        