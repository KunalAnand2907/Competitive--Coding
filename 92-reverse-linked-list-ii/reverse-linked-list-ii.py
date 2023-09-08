# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # T(n): O(n), S(n): O(1)
        Dn = ListNode(0,head)
        # Phase 1: Get at the Left Node and PrevL to point 1 prev of Left Node
        lprev,curr = Dn,head
        for i in range(0,left-1):
            lprev,curr = curr,curr.next
        # Phase 2 : To break the Links or reverse the LL from L-->R
        Prev = None
        for i in range(0,right-left+1):
            tmp = curr.next
            curr.next = Prev
            Prev,curr = curr,tmp
        # Phase 3: The lprev should point at last node and lp.next should point at Prev (Right Node)
        lprev.next.next = curr
        lprev.next = Prev
        return Dn.next
        