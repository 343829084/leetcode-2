# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        this_node = root
        while this_node is not None:
            result.append(this_node.val)
            if this_node.right:
                stack.append(this_node.right)
            if this_node.left:
                this_node = this_node.left
            else:
                this_node = stack.pop() if stack else None
                
        return result