# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymmetricTree(p, q):
            if not p and not q:
                return True
            if not (p and q):
                return False
            if p.val != q.val:
                return False
            return isSymmetricTree(p.left, q.right) and isSymmetricTree(p.right, q.left)
        
        if not root:
            return True
        return isSymmetricTree(root.left, root.right)
        