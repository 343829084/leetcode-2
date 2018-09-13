# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        p = head
        while True:
            if p is None:
                return False
            if id(p) in s:
                return True
            s.add(id(p))
            p = p.next
            
        