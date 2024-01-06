class Solution(object):
    def twoSum(self, nums, target):
        # Hash Map - T(n), S(n) - O(n)
        prevMap = {} # val,idx -- where i am storing the Prev Diff not the number and its index w.r.t Array
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap: # means we get the prev ind and the curr ind of the sum matching to target
                return [prevMap[diff],i]
            prevMap[n]=i
        