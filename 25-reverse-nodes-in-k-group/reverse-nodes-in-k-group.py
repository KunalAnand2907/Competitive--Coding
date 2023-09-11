# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1.) BC: when empty LL or k==1 ~ No reversal 
        if not(head) or k==1:
            return head
        Dn = ListNode(0,head)
        cur,nex,pre = Dn,Dn,Dn
        cnt = 0
        # 2.) Count the len of LL
        while(cur.next):
            cur = cur.next
            cnt+=1
        # 3.) Will keep doing till >=k
        while(cnt>=k):
            # Re-assign cur & next after each reversal of LL of Length K
            cur = pre.next
            nex = cur.next
            # Main Algo
            for i in range(1,k):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            # Move the prev to cur
            pre = cur
            cnt-=k
        return Dn.next
        