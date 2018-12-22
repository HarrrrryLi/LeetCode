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
        
        result = ListNode(0)
        r_temp = result
        c = 0
        
        while l1 or l2 or c==1:
            val = c  
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            r_temp.next = ListNode(val%10)
            c = val/10
            r_temp = r_temp.next
        
        return result.next