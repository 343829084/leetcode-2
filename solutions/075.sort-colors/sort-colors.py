class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = [0, 0, 0]
        for num in nums:
            l[num] += 1
        
        while nums:
            nums.pop()
        
        temp = [0] * l[0] + [1] * l[1] + [2] * l[2]
        
        nums.extend(temp)
        