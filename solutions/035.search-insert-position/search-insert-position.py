class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.findPrePos(nums, 0, len(nums)-1, target) + 1
            
    def findPrePos(self, nums, left, right, target):
        if left > right:
            return -1
        if left == right:
            if target <= nums[left]:
                return left - 1
            else:
                return left
            
        mid = (left + right) / 2 + 1
        if target <= nums[mid]:
            return self.findPrePos(nums, left, mid-1, target)
        else:
            return self.findPrePos(nums, mid, right, target)