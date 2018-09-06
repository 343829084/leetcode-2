class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self._search(nums, 0, len(nums)-1, target)
    def _search(self, nums, left, right, target):
        if not nums or left > right:
            return -1
        
        mid = (left+right)/2
        if nums[mid]==target:
            return mid
        if nums[left]<=nums[mid]:
            if nums[left]<=target<nums[mid]:
                return self._search(nums, left, mid-1, target)
            else: 
                return self._search(nums, mid+1, right, target)
        else:
            if nums[mid]<target<=nums[right]:
                return self._search(nums, mid+1, right, target)      
            else: 
                return self._search(nums, left, mid-1, target)
