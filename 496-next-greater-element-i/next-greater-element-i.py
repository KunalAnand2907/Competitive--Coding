class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Method 1: Brute Force
        # T(n): O(n.n-1) ~ O(n**2) - independant nested for loops , S(n): O(len(nums2))
        # Dict and 2 Nested Dep For loops
        # d={}
        # for i in range(len(nums2)):
        #    next=-1
        #    for j in range(i+1,len(nums2)):
        #        if nums2[i]<nums2[j]:
        #             next = nums2[j]
        #             break
        #    d[nums2[i]]=next
        # return [d[k] for k in nums1]
        # Method 2: Monotonic Dec Stack with 2 Virtual Pass - T(n): O(n+n), S(n):O(len(nums2))
        st = [] # Mon Dec Order
        d = {k:-1 for i,k in enumerate(nums2)}
        n = len(nums2)
        for i in range(n-1,-1,-1):
            while(st!=[] and st[-1]<=nums2[i]):
                st.pop()
            if st!=[]:
                d[nums2[i]] = st[-1]
            st.append(nums2[i])
        return [d[k] for k in nums1]
        
        
        