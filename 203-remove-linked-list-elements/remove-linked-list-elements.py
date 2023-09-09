# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # T(n): O(n), S(n): O(1) -- 2 Pointers
        dn = ListNode(0,head)
        Prev,curr = dn,head
        while curr:
            nxt = curr.next
            if curr.val==val:
                Prev.next = nxt
            else:
                Prev = curr
            curr = nxt
        return dn.next
            
                
        