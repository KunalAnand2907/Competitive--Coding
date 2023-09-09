# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        # 2 dn with 2 Pointers, T(n): O(n), S(n): O(1)
        left,right = ListNode(), ListNode()
        ltail,rtail = left,right

        while head:
            if head.val<x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        ltail.next = right.next
        rtail.next = None
        return left.next