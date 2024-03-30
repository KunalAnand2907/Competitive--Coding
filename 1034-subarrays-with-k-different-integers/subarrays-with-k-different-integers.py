class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        # Sliding wind+ HastTab+ Math - T(n) -O(n), S(n) -O(k) ~ atmost k elements
        def atmost(k):
           # Ht keeps count of ele's
           count = Counter()
           i,res=0,0 # res - total no of subarrays with atmost k diff int
           for j in range(0,len(nums)):
               # if ele not present in count, dec the k
               if count[nums[j]]==0:
                   k-=1
               # 2 CASES: if not present:add & inc the count of ele, if present: inc the count of ele
               count[nums[j]]+=1
               # when k=-1 <0
               while k<0:
                   # first we dec the count at initial pos - means also we have more than k diff char's now
                   count[nums[i]]-=1
                   # if count at i=0 inc the k
                   if count[nums[i]]==0:
                       k+=1
                   # 2 cases: when count =0 or count!=0 we need to increment i for next subarray
                   i+=1
               res+=j-i+1
           return res
        return atmost(k)-atmost(k-1)


        