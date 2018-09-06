class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        pre = nums[0]
        length = 1
        for i, num in enumerate(nums):
            if num == pre:
                continue
            else:
                nums[length] = num
                pre = num
                length += 1
                
        return length
        