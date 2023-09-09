class Solution(object):
    def combinationSum4(self, nums, target):
        # DP Memoization(Top Down): T(n): O(n.m), S(n):O(n), where n in target & m is the size of nums
        dp={0:1}
        for total in range(1,target+1):
            dp[total] = 0
            for n in nums:
                dp[total]+=dp.get(total-n,0)

        return dp[target]