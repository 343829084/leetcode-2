# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        lvl = 1
        while True:
            temp = []
            for node in stack:
                if not node.left and not node.right:
                    return lvl
                temp.extend([node.left, node.right])
            stack = [node for node in temp if node]
            lvl += 1
        return lvl
            