# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        root = preorder[0]
        root_in_inorder = inorder.index(root)
        in_left = inorder[:root_in_inorder]
        left_len = len(in_left)
        in_right = inorder[root_in_inorder + 1 :]
        
        pre_left = preorder[1: 1+left_len]
        pre_right = preorder[1+left_len:]
        
        tree = TreeNode(root)
        tree.left = self.buildTree(pre_left, in_left)
        tree.right = self.buildTree(pre_right, in_right)
        
        return tree
        