class Solution(object):
    def numSubarraysWithSum(self, nums, S):
        # 1.) Brute Force - Hash Table, T(n),S(n) -O(n),O(n)
        # Count the occurrence of prefix sum
        # cnt = Counter({0:1})
        # psum,res=0,0
        # for j in range(len(nums)):
        #     # computing the prefix sum
        #     psum+=nums[j]
        #     # updating the res 
        #     res+=cnt[psum-S]
        #     # Inc the psum occurrence
        #     cnt[psum]+=1
        # return res

        # 2.) Better Approach - Sliding Window - T(n)-O(n), S(n) -O(1)
        # base cond
        def atmost(S):
           if S<0: return 0
           res,i=0,0
           for j in range(len(nums)):
               S-=nums[j]
               while S<0:
                   S+=nums[i]
                   i+=1
               # at each pos tell the number of subarrays with sum ~ goal
               res+=j-i+1
           return res
        return atmost(S) - atmost(S-1)