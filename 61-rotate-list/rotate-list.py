# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        # 2 Pointer with len, T(n): O(n) , S(n): O(1)
        # 1.) BC - when list is empty
        if not(head):
            return head
        len,tail = 1,head
        # 2.) To find the length of ll, and tail pointer to point at last node
        while tail.next:
            tail= tail.next
            len+=1
        # 3.) No of Rotations
        k = k%len
        if k==0: # k==0 or k==len(LL)
            return head
        # If k</> len then do the below one
        cur = head
        for i in range(0,len-k-1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead
               