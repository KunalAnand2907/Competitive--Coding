# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 2 pointers, T(n): O(n+m), S(n): O(1)
        l1,l2 = headA,headB
        while(l1!=l2 and l1!=None and l2!=None):
            l1 = l1.next
            l2 = l2.next
            if l1==l2: # when common node exists, or when both equal len and no common node, or when not equal len & also no common ele then also will become null at same point
                return l1
            if l1==None:
                l1 = headB
            if l2 == None:
                l2 = headA
        return l1 # both are empty
        
        