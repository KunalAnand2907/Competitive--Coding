class Solution(object):
    def isPerfectSquare(self, num):
        # T(n) - O(root n)
        for i in range(1,int(num**0.5)+1):
            if i*i==num:
                return True
            elif i*i>num:
                return False
        return False
        # # T(n)-O(logn), S(n): O(1)- Binary Search
        # l,r=1,num
        # while(l<=r):
        #     mid=(l+r)//2
        #     if mid*mid>num:
        #         r=mid-1 # remove the mid and upper half
        #     elif mid*mid<num:
        #         l=mid+1# remove the mid and lower half
        #     else:
        #         return True
        # return False