import math

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = 0
        
        # "冒泡排序"
        # for j in range(len(nums)):
        #     for i in range(len(nums)-1-j):
        #         if nums[i] > nums[i+1] :
        #             tem = nums[i]
        #             nums[i] = nums[i+1] 
        #             nums[i+1] = tem
        #         i += 1
        #     j +=1            
        #nums.sort()
        self.quicksort(nums,0,len(nums)-1)
        
        n = 1
        while n <=  math.ceil(len(nums)/2):
            maxsum = maxsum + nums[2*n-2]
            n += 1
            
        return maxsum
        
        
    def quicksort(self,lists,left,right):
        if left >= right:
            return lists
        low = left
        high = right
        key = lists[left]
        while left < right:
            while left < right and lists[right] >= key:
                right -= 1
            lists[left] = lists[right]
            while left < right and lists[left] <= key:
                left += 1
            lists[right] = lists[left]
        lists[right] = key
        self.quicksort(lists,low,left - 1)
        self.quicksort(lists,left+1,high)
        return lists

            
        
        