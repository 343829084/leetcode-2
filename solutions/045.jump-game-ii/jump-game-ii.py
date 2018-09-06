class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp超时
#         dp = [0 for num in nums]
#         for i, num in enumerate(nums):
#             stps = float('inf')
#             for j in range(i):
#                 if j + nums[j] >= i:
#                     stps = min(stps, dp[j] + 1)
#             dp[i] = stps if i != 0 else 0
            
#         return dp[-1]
        # 贪心
        stps, reach, this_reach = 0, 0, 0
        size = len(nums) - 1
        for i, num in enumerate(nums):
            if (i <= reach and reach < size and (i+num)>reach):
                this_reach = max(this_reach, i + num)
            if (i == reach and this_reach > reach):
                reach = this_reach
                stps += 1
        return stps
                
                