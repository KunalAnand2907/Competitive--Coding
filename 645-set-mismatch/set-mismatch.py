class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        s=n*(n+1)//2
        missing = s - sum(set(nums))
        duplicate = sum(nums) - sum(set(nums))
        return [duplicate,missing]
        