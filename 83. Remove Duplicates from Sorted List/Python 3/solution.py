# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        pre = head
        current = head.next
        val = head.val

        while current:
            if current.val == val:
                pre.next = current.next
                current = pre.next
            else:
                pre = current
                val = current.val
                current = current.next

        return head
