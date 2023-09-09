# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        # T(n): O(n**2) - Best Case & O(n) - Best Case (Traversal of LL), S(n): O(1)
        Dn = ListNode(0,head)
        Prev,curr = head, head.next
        while curr:
            # 1.) if till know the list is in sorted order
            if curr.val>=Prev.val:
                Prev,curr = curr, curr.next
                continue
        # 2.) If not in sorted order, so check for the position after which we need to add the node(add in -btw, add before the head)
            tmp = Dn
            while(curr.val>tmp.next.val):
                tmp = tmp.next
            Prev.next = curr.next
            curr.next = tmp.next
            tmp.next = curr
            curr = Prev.next
        return Dn.next


    