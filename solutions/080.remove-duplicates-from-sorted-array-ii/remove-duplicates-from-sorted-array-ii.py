class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        pre, count, length = nums[0], 1, 1
        for i in range(1,len(nums)):
            num = nums[i]
            if num == pre and count ==1:
                count += 1
                length += 1
                nums[length-1] = num
            elif num != pre:
                pre, count = num, 1
                length += 1
                nums[length-1] = num
        return length
        