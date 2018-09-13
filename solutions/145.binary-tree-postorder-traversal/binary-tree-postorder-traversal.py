# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        this_node = root
        while this_node:
            left, right = this_node.left, this_node.right
            this_node.left, this_node.right = None, None
            if left:
                stack.append(this_node)
                if right:
                    stack.append(right)
                this_node = left
            elif right:
                stack.append(this_node)
                this_node = right
            else:
                result.append(this_node.val)
                this_node = stack.pop() if stack else None
        return result
                
        