"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        # 2 Passes & HM, T(n): O(n)+O(n), S(n): O(n)
        # First Pass
        otc = {None: None} # Handles the edge cases
        cur = head
        while cur:
            copy = Node(cur.val)
            otc[cur] = copy # {None:None,Node(7): Node(7)} if not none cur, then cur points to 2nd key
            cur = cur.next
        # Second Pass
        cur = head
        while cur:
            copy = otc[cur]
            copy.next = otc[cur.next]
            copy.random = otc[cur.random]
            cur = cur.next
        return otc[head]
