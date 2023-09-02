# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        # 1.) Merge Sort in LL
        # Base cond: if head empty or only 1 node return head itself
        if not(head) or not(head.next):
            return head
        # split the list into 2 halfs
        left,right = head, self.getMid(head)
        tmp = right.next # store the right node
        right.next = None # to split it in 2 halfs
        right = tmp # right takes the right node
        
        #Recursive MS and Merge
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left,right)

    def getMid(self,head):
        slow, fast= head,head.next
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        return slow # mid node
        
    def merge(self,left,right):
        # Create a dummy node
        tail = dummy = ListNode()
        while left and right: # Not None
             if left.val < right.val:
                 tail.next = left
                 left = left.next
             else:
                 tail.next = right
                 right = right.next
             tail=tail.next
             
        if left:
                 tail.next = left
        elif right:
                 tail.next = right
        return dummy.next
        