# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    res = None
    def findmax(self, root):
        if root == None:
            return 0
        else:
            max_l = self.findmax(root.left)
            max_r = self.findmax(root.right)
            max_s = max(max(max_l, max_r) + root.val, root.val)
            max_top = max(max(max_s, max_l+max_r+root.val), root.val)
            if self.res == None:
                self.res = max_top
            else:
                self.res = max(self.res, max_top)
            return max_s
     
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findmax(root)
        return self.res
        