class Solution(object):
    def climbStairs(self, n):
        # Recusrsion: T(n): O(2^n), S(n): O(n) - Aux Space
        #  if n==0:
        #     return 1
        # elif n==1:
        #     return 1
        # l = self.climbStairs(n-1)
        # r = self.climbStairs(n-2)
        # return l+r
        # Via Dp with no external Array - T(n): O(n), S(n): O(1)
        one,two=1,1
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one
