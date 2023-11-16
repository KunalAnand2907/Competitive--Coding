class Solution(object):
    def findDifferentBinaryString(self, nums):
        # Backtracking with Hash Set - T(n)=O(n.n) as for each cur of length n we call backtrack n times so as to recah the base cond and return the res
        strset = { s for s in nums} # covert array into set, can be done by set(nums)
        def backtrack(i,cur): # O(n)
            # Base Cond
            if i==len(nums):
                res = "".join(cur)
                return None if res in strset else res
            res = backtrack(i+1,cur)
            # 1st check if res not None
            if res: return res
            # 2nd Check: we have not found the res so we update "0" to "1" at part ith position in cur & then again backtrack 
            cur[i] = "1"
            res = backtrack(i+1,cur)
            if res: return res

        return backtrack(0,['0' for s in nums]) # O(n)