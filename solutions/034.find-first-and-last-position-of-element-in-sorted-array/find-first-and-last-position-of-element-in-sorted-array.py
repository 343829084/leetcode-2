class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findLeftPos(nums, 0, len(nums)-1, target), self.findRightPos(nums, 0, len(nums)-1, target)]
    
    def findRightPos(self, nums, left, right, target):
        if left > right:
            return -1
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
            
        mid = (left + right) / 2 + 1
        if target < nums[mid]:
            return self.findRightPos(nums, left, mid-1, target)
        else:
            return self.findRightPos(nums, mid, right, target)
    
    def findLeftPos(self, nums, left, right, target):
        if left > right:
            return -1
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
            
        mid = (left + right) / 2
        if target <= nums[mid]:
            return self.findLeftPos(nums, left, mid, target)
        else:
            return self.findLeftPos(nums, mid+1, right, target)
        