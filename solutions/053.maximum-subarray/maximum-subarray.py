class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if all([num <=0 for num in nums]):
            return max(nums)
                
        left = 0
        max_sum = 0
        this_sum = 0
        for num in nums:
            this_sum += num
            if this_sum > max_sum:
                max_sum = this_sum
            if this_sum < 0:
                this_sum = 0
        return max_sum