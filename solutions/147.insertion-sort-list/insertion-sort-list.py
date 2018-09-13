# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        sorted_list = ListNode(0)
        p = head
        while p:
            self.insert(sorted_list, p)
            p = p.next
        return sorted_list.next
    
    def insert(self, sorted_list, p):
        this_node = sorted_list
        next_node = this_node.next
        while next_node:
            if p.val < next_node.val:
                q = ListNode(p.val)
                q.next = next_node
                this_node.next = q
                return
            
            this_node = next_node
            next_node = next_node.next
        
        this_node.next = ListNode(p.val)
        
        
        
            
        