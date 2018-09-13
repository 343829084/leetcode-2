# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._getHeightOf(root) >= 0
    
    def _getHeightOf(self, root):
        """
        获取树的高度，如果不平衡则返回-1
        """
        if not root:
            return 0
        
        left_height = self._getHeightOf(root.left)
        right_height = self._getHeightOf(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
        