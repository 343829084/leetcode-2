# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        level_traversal = []
        queue = []
        this_node = (0, root)
        while this_node[1]:
            level_traversal.append(this_node)
            if this_node[1].left:
                queue.append((this_node[0] + 1, this_node[1].left))
            if this_node[1].right:
                queue.append((this_node[0] + 1, this_node[1].right))
            this_node = queue.pop(0) if queue else (None, None)
        
        f = level_traversal.pop(0)
        while level_traversal:
            n = level_traversal.pop(0)
            f[1].next = n[1] if f[0] == n[0] else None
            f = n
            