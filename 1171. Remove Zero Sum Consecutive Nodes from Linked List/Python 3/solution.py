# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        while True:
            if not head:
                break
            dp = {0: None}
            temp = head
            result = 0
            while temp:
                result += temp.val
                if result not in dp:
                    dp[result] = temp
                    temp = temp.next
                else:
                    pre, end = dp[result], temp
                    break
            else:
                break

            if pre == None:
                head = temp.next
            else:
                pre.next = temp.next

        return head
