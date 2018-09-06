# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = []
        level = 0
        this_node = (0, root)  # namedtuple is better
        while this_node:
            level = this_node[0]
            if len(result) == level + 1:
                if level % 2 == 0:
                    result[this_node[0]].append(this_node[1].val)
                else:
                    result[this_node[0]].insert(0, this_node[1].val)
            else:
                result.append([this_node[1].val])
            if this_node[1].left:
                queue.append((level+1, this_node[1].left))
            if this_node[1].right:
                queue.append((level+1, this_node[1].right))
            this_node = queue.pop(0) if queue else None
        return result
        