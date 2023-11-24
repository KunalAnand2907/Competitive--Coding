class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # T(n): O(n.n-1) ~ O(n**2) - independant nested for loops , S(n): O(len(nums2))
        # Dict and 2 Nested Dep For loops
        d={}
        for i in range(len(nums2)):
           next=-1
           for j in range(i+1,len(nums2)):
               if nums2[i]<nums2[j]:
                    next = nums2[j]
                    break
           d[nums2[i]]=next
        return [d[k] for k in nums1]
        
        
        