# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        # 1.) 2 Pointer App with Dummy Node, T(n):O(n), S(n): O(1) -- hndles all the cases, 1 node & that only delete
        # 2.) 3 Pointer App. with Dummy Node, T(n): O(n), S(n): O(1)
        dn = ListNode(0,head)
        left,right = dn, head
        while n>0 and right:
            right = right.next
            n-=1
        while right:
            right = right.next
            left = left.next
        if n<=0:
            left.next = left.next.next

        return dn.next
