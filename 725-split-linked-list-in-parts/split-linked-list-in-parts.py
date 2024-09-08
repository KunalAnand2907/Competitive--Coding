# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        # T(n): O(n), S(n): O(1), None ~ [], [[1,2],[3]] ~ Node1-->Node2, Node3, Node4
        len,curr = 0,head
        # 1.) Find the Len of LL
        while(curr):
            curr=curr.next
            len+=1
        # 2.) Find the BL & Extra Nodes per each LL
        base_len,remain = len//k,len%k
        res,curr = [], head
        for i in range(k):
            res.append(curr)
            for j in range(base_len  - 1 + (1 if remain else 0)):
                if not(curr):
                    break
                curr = curr.next
            # dec remainder only if it is >=1
            remain -= (1 if remain else 0)
            # break the LL, by making it .next point to Null, and move the curr to curr.next
            if curr:
                curr.next,curr = None,curr.next
        return res
        