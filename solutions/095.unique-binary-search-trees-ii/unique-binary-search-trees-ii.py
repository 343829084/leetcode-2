# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from itertools import product

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self._generateTrees(1, n)
        
    def _generateTrees(self, left, right):
        if left > right:
            return [None]
        result = []
        for i in range(left, right+1):          # traversal
            left_subs = self._generateTrees(left, i-1)
            right_subs = self._generateTrees(i+1, right)
            
            _ = product(left_subs, right_subs)
            
            for l, r in _:
                this_node = TreeNode(i)
                this_node.left, this_node.right = l, r
                result.append(this_node)
        return result
        
        