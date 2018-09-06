# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_list= ListNode(0)
        cur_node = sum_list

        sum = 0
        while True:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next

            cur_node.val = sum % 10
            sum /= 10
            if l1 != None or l2 != None or sum != 0:
                cur_node.next = ListNode(0)
                cur_node = cur_node.next
            else:
                break

        return sum_list
        