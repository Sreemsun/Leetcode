"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = {None : None}
        n = head
        while n:
            old[n] = Node(n.val)
            n = n.next
        n = head
        copy = old[n]
        while n:
            copy.next = old[n.next]
            copy.random = old[n.random]
            copy = copy.next
            n = n.next
        return old[head]



