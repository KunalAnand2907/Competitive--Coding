class Solution:
    def isHappy(self, n: int) -> bool:
        # T(n):O(n), S(n): O(n)
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfsqaures(n)
            if n==1:
                return True
        return False

    def sumOfsqaures(self,n):
        out = 0
        while n!=0:
            digit = n%10 # one's place digit
            digit = digit**2
            out +=digit
            n = n//10
        return out

        