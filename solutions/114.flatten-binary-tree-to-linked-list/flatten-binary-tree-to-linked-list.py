# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        this_node = root
        while this_node:
            if this_node.right:
                stack.append(this_node.right)
            if this_node.left:
                stack.append(this_node.left)
            this_node.left = None
            next_node = stack.pop() if stack else None
            this_node.right = next_node
            this_node = next_node
            