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
        copy = preroot = Node(-1, head, None)
		
        while head:
            orig_next = head.next
            head.next = copy.next = Node(head.val, None, head.random)
            head, copy = orig_next, copy.next
        
        copy = preroot.next
        while copy:
            copy.random = copy.random.next if copy.random else None
            copy = copy.next
            
        return preroot.next