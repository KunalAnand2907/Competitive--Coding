class Solution(object):
    def maxLength(self, arr):
        # Method 1: Backtracking + set: T(n): O(2**n.m), S(n): O(n) - set/recusrive stack
        chS = set() # will contain all uni curr chars of a string
        def overlap(chS,s):
            c = Counter(chS)+Counter(s)
            return max(c.values())>1 # true if count of any char 2 after concatenation of 2 sub seq's

        def Backtrack(i): # i is the index in array
            # Base Cond/ or the stopping cond of bactrack to ret something
            if i==len(arr):
                return len(chS)
            res=0 # max length of conc string
            if not(overlap(chS,arr[i])):
                for c in arr[i]:
                     chS.add(c)
                res=Backtrack(i+1)
                for c in arr[i]:
                    chS.remove(c)
            return max(res,Backtrack(i+1)) # Don't concatenate if overlaps
      

        # returning & calling the helper fn    
        return Backtrack(0)

        # Method 2: Bit Masking
        