# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # 2 Loops with Curr Pointer, T(n): O(n) , S(n): O(1)
        cur = head
        while cur:
            while cur.next and cur.next.val==cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

        