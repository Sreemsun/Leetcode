# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        n = head
        while n :
            if n.next and n.val == n.next.val:
                n.next = n.next.next
            else:
                n = n.next
        return head