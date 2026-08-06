# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        a = []
        if not head or not head.next:
            return head
        while head:
            b = head.val
            a.append(b)
            head = head.next
            m = n
        while m:
            m.val = a[-1]
            a.pop(-1)
            m = m.next
        return n
