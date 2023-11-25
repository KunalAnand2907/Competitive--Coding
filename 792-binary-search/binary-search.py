class Solution(object):
    def search(self, nums, target):
        # T(n)-O(logn), S(n)-O(1)
        l,r=0,len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if nums[m]>target:
                r=m-1# eliminate the right half as the ele will be in left half
            elif nums[m]<target:
                l=m+1 # eliminate the lower half as the ele will be in right half
            else:
                return m
        return -1 # target not found