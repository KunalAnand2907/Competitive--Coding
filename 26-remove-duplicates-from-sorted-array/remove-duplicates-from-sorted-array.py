class Solution(object):
    def removeDuplicates(self, nums):
        # T(n): O(n), S(n): O(1)
        for i in range(0,len(nums)):
            j=i+1
            while j<len(nums) and nums[j]==nums[i]:
                nums.pop(j)
        return len(nums)
        