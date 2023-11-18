class Solution(object):
    def maxFrequency(self, nums, k):
        # Sort & Sliding Window - T(n) - O(nlogn), S(n) - O(1)
        nums.sort()
        l,r=0,0
        res,total = 0,0 # res is max wind size(max freq of special ele), sum of all ele in curr wind
        while(r<len(nums)):
            total+=nums[r]
            while(nums[r]*(r-l+1)>total+k): # invalid we need to shrink our window
                 total-=nums[l]
                 l+=1
            res = max(r-l+1,res)
            r+=1
        return res
