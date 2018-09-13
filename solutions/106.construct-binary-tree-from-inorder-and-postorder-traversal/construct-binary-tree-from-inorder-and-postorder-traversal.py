# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder or not inorder:
            return None
        
        root = postorder[-1]
        root_in_inorder = inorder.index(root)
        in_left = inorder[:root_in_inorder]
        left_len = len(in_left)
        in_right = inorder[root_in_inorder + 1 :]
        
        post_left = postorder[:left_len]
        post_right = postorder[left_len:-1]
        
        tree = TreeNode(root)
        tree.left = self.buildTree(in_left, post_left)
        tree.right = self.buildTree(in_right, post_right)
        
        return tree
        