class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Math+Recursion(Divide & conquer: 2^5 = 2^2.2^2.2): T(n):(log2n),S(n): O(n), Asked in Arcesium
        def help(x,n):
            # base cases
            if x==0:
                return 0
            elif n==0:
                return 1
            res = help(x*x,n//2)
            # res = res*res
            return x*res if n%2 else res
        res = help(x,abs(n))
        return res if n>=0 else 1/res