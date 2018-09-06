# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        this_node = root
        while this_node:
            if this_node.right:
                stack.append(this_node.right)
            if this_node.left:
                left = this_node.left
                this_node.left, this_node.right = None, None
                stack.append(this_node)
                this_node = left
            else:
                result.append(this_node.val)
                this_node = stack.pop() if stack else None
        return result
        