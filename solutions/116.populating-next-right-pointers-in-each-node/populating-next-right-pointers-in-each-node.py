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
            return;
        this_level = root 
        while this_level.left:
            this_node = this_level;
            while this_node:
                this_node.left.next = this_node.right;
                if this_node.next:
                    this_node.right.next = this_node.next.left;
                this_node = this_node.next;
            
            this_level = this_level.left;
        