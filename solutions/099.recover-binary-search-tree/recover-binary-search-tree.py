# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [(root, root.val)] + self.inorderTraversal(root.right)
        
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        inorder_traversal = self.inorderTraversal(root)
        len_tree = len(inorder_traversal)
        node1, node2 = None, None
        for i, (node, val) in enumerate(inorder_traversal):
            next_node, nextval = (inorder_traversal[i+1][0], inorder_traversal[i+1][1]) if len_tree > i+1 else (None, None)
            if not (nextval is None) and val > nextval:
                if not node1:
                    node1, node2 = node, next_node
                else:
                    node2 = next_node
                    break
        if node1 and node2:
            node1.val, node2.val = node2.val, node1.val
            
            
        