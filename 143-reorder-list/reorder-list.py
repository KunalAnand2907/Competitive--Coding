# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        # 1.) Finding the middle works for both even, odd 
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # return slow
        
        #2.) Reverse the second half ll including the middle in even and not including the middle in odd length
        second = slow.next
        slow.next = None
        prev = None
        while second!=None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #3.) Merging both parts, one by one, not merging 2 sorted lists
        first=head
        second=prev
        while second:
            t1,t2 = first.next,second.next
            first.next = second
            second.next = t1
            first,second = t1,t2
        