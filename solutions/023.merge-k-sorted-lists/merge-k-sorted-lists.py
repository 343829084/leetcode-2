# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        m = len(lists)/2
        return self.mergeTwoLists(self.mergeKLists(lists[:m]), self.mergeKLists(lists[m:]))
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        l = ListNode(0)  # header
        ll = l
        while l1 and l2:
            if l1.val < l2.val:
                ll.next = ListNode(l1.val)
                l1 = l1.next
            else:
                ll.next = ListNode(l2.val)
                l2 = l2.next
            ll = ll.next
        if l1:
            ll.next = l1
        if l2:
            ll.next =l2
        return l.next
        