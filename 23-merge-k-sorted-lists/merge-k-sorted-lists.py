# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # T(n): O(logk.n), S(n): O(1)
        # Edge Case: if K==0 then return None
        if len(lists)==0 or lists[0]==[]:
            return None
        #2.) when k>1, for loop increment the k 
        while len(lists)>1:
            ml=[]
            for i in range(0,len(lists),2):
                # L1 takes the first list
                l1=lists[i]
                # L2 takes the second list only if i+1 < k
                l2=lists[i+1] if (i+1)<len(lists) else None
                # append these list in ml and call the mergeTwoLists function, that compairs one by one element of both lists 
                ml.append(self.mergeTwoLists(l1,l2))
            # Lists takes the ml which is only one lists
            lists=ml
        return lists[0]
    
    def mergeTwoLists(self,l1,l2):
        # initialize a dummy node as one sorted list, no value as 0 can be in 2 lists
        dummy = ListNode()
        # pointer initially points to dummy node runs 1 less than the l1 & l2 pointer
        curr=dummy
        # 1.) If both are None
        if l1 == None and l2==None:
            return None
        # 2.) If both length equal and are not equal to None
        while(l1 and l2):
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            # move the curr pointer after satisfying any one condition 
            curr=curr.next
        # 3.) when not of equal length or l1|l2 None
        if l1:
            curr.next=l1
        else:
            curr.next=l2
        return dummy.next