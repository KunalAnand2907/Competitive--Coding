# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0,head)
        prev,cur = head, head.next # 4, 2
        while cur:
            if cur.val >= prev.val: # 2>4 do nothing
                prev,cur=cur,cur.next # means no swapping and iterate both prev, cur by 1 
                continue
            tmp = dummy
            while cur.val >tmp.next.val: # 2 > 4 -- no
                tmp=tmp.next # iterate the temp
            # find the spot for 2 
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        return dummy.next
    

    