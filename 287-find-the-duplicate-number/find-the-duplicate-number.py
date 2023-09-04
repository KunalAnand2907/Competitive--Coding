class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Cycle Algo - T(n) - O(n), S(n)-O(1) - 2 pointer approach ~ same code to ll cycle 2
        # Ex: - [1,3,4,2,2] - LL Node -- 0->3->2->4 back to 2 - the first ind always is out of the range of [1,n]
        # Phase 1 - Tells that the cycle exists
        slow,fast=0,0
        while (True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break # stop the first slow - 1st Intersection Point
        # Phase 2 - return the start node of the cycle & is the duplicate number
        slow2=0
        while (True):
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2: # 2nd intersection 
                return slow # can return either of the Two