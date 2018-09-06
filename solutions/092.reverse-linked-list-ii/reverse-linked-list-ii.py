# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m == n:
            return head
        
        pre, cur, nex = None, head, head.next
        for i in range(m-1):
            pre, cur, nex = cur, nex, nex.next
        left_pre = pre
        left = cur
        
        for i in range(n-m):
            nex_new =nex.next
            nex.next = cur
            cur, nex = nex, nex_new
        right = cur
        right_nex = nex
        
        left.next = right_nex
        if left_pre is None:
            head = right
        else:
            left_pre.next = right
        
        return head
        