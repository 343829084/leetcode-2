# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        p, q = root, root
        for i in range(n):
            q = q.next
        
        while q.next:
            p, q = p.next, q.next
        tmp = p.next.next
        p.next = tmp
        
        return root.next