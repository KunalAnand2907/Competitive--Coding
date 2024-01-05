class Solution(object):
    def lengthOfLIS(self, nums):
        # 1.) Recur+ Memo, T(n): O(n.n), S(n): O(n.n)+O(n), 10^10 > 10^5 size of array - TLE
        # def f(ind,prev_i,dp):
        #     # 2 BC's
        #     if ind==n:
        #         return 0
        #     if dp[ind][prev_i+1]!=-1:
        #         return dp[ind][prev_i+1]
        #     # Not take
        #     len = 0+f(ind+1,prev_i,dp)
        #     # Take
        #     if(prev_i==-1 or nums[ind]>nums[prev_i]):
        #         len = max(len,1+f(ind+1,ind,dp))
        #     dp[ind][prev_i+1]=len
        #     return dp[ind][prev_i+1]
        

        # dp = [[-1]*(n) for _ in range(n+1)]
        # return f(0,-1,dp)
        # 2.) Cache list having 1 length at each position
        # lis = [1]*len(nums)
        # # i runs in reverse order
        # for i in range(len(nums)-1,-1,-1):
        #     # j runs in inc orer till the len(nums)--check at i+1 positon
        #     for j in range(i+1,len(nums)):
        #         #4<3 not works, 2<4,3 --max(1,2),max(2,2)--2 so at lis[1]=2
        #         if nums[i]<nums[j]:
        #             lis[i]=max(lis[i],1+lis[j])
        # return max(lis)
        # 3.) Dp with Tab + Space Optim, T(n): O(n^2), S(n): O(n)
        # next = cur = [0]*(len(nums)+1)
        # for i in range(len(nums)-1,-1,-1):
        #     p_i=i-1
        #     while(p_i>=-1):
        #         l = 0 + next[p_i+1] # not take
        #         if(p_i==-1 or nums[i]>nums[p_i]): # take
        #             l = max(l,1+next[i+1])
        #         cur[p_i+1]=l
        #         p_i-=1
        #     next = cur
        # return next[-1+1]
        # 4.) Dp with Tab (New Method) ~ Also used to write Print LIS
        dp = [1]*len(nums)
        maxi = 1
        for i in range(0,len(nums)):
            for p_i in range(0,i):
                if nums[p_i]<nums[i]:
                    dp[i] = max(dp[i],1+dp[p_i]) # updating the LIS at that part Index
            maxi = max(maxi,dp[i]) # Lis from all LIS at part ind
        return maxi