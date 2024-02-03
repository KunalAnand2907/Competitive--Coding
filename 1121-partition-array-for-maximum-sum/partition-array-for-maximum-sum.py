class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        # Partition Dp -- Front Partition
        # 1.) Recur + Memo, T(n): O(n.k), S(n): O(n)+O(n)
        n = len(arr)
        # def f(ind):
        #     # 1.) BC 1 
        #     if ind==n: return 0
        #     # 1.) BC 2
        #     if dp[ind]!=-1: return dp[ind]
        #     # 2.) Main Algo
        #     leni,maxi,maxA=0,-1e9,-1e9
        #     for j in range(ind,min(n,ind+k)):
        #         leni+=1
        #         maxi = max(maxi,arr[j])
        #         Sum = leni*maxi + f(j+1)
        #         maxA = max(maxA,Sum)
        #     dp[ind]=maxA
        #     return dp[ind]
        # dp = [-1]*n
        # return f(0)
        # 2.) Dp with Tab, T(n): O(n.k), S(n): O(n)
        dp = [0]*(n+1)
        dp[n]=0
        for i in range(n-1,-1,-1): # in rec moves from 0-n-1, here from base case to 0 (n-1) to 0
            leni,maxi,maxA=0,-1e9,-1e9
            for j in range(i,min(n,i+k)):
                leni+=1
                maxi = max(maxi,arr[j])
                Sum = leni*maxi + dp[j+1]
                maxA = max(maxA,Sum)
            dp[i]=maxA # for each index we are taking the max sum of diff partitions formed
        return dp[0]
