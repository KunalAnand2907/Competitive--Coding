class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        # Dp with Squares
        # 1.) Dp with Tab, T(n): O(n.m), S(n): O(n.m)
        n,m=len(mat),len(mat[0])
        dp = [[0]*m for _ in range(n)]
        # Copy the first Row & Col as it is
        for j in range(0,m):
            dp[0][j]=mat[0][j]
        for i in range(0,n):
            dp[i][0]=mat[i][0]
        
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][j]==0: dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
        Sum=0
        for i in range(0,n):
            for j in range(0,m):
                Sum+=dp[i][j]
        return Sum
        