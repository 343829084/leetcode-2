class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        max_num = max(nums)
        if max_num < 1:
            return 1
        
        l = [0]*(max_num + 1)
        for num in nums:
            if num > 0:
                l[num] += 1
                
        p = 1
        while p < len(l) and l[p] :
            p += 1
        
        return p
        