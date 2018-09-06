class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 如果能跳到 A[i], 则 A[j](0<=j<=i)都能到达
        # 如果能到达的最大高度比A.size大，则能到达A[-1]
        reach = 0
        size = len(nums) - 1
        for index, num in enumerate(nums):
            if (index <= reach and reach < size):
                reach = max(reach, index + num)
                
        return reach >= size