# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def path(self, root):
        result = []
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        
        l = self.path(root.left)
        r = self.path(root.right)
        if l:
            result += [[root.val] + x for x in l]
        if r:
            result += [[root.val] + x for x in r]
        return result

        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path_lst = self.path(root)
        _sum = 0
        for p in path_lst:
            this = 0
            for digit in p:
                this = this * 10 + digit
            _sum += this
            
        return _sum
        