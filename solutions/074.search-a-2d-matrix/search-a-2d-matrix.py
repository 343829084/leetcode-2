class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = self.findRow(matrix, target)
        if row == -1:
            return False
        return self.findTarget( matrix[row], target) >= 0
        
    def findRow(self, matrix, target):
        if not matrix:
            return -1
        if not len(matrix[0]):
            return False
        left, right = 0, len(matrix)-1
        while left < right:
            mid = (left + right) / 2 + 1
            if target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid
        if target < matrix[left][0]:
            return left -1
        return left
    
    def findTarget(self, l, target):
        if not l:
            return -1
        
        left, right = 0, len(l)-1
        while left < right:
            mid = (left + right) / 2 + 1
            if target < l[mid]:
                right = mid - 1
            else:
                left = mid
        
        if l[left] == target:
            return left
        return -1