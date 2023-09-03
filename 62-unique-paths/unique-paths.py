class Solution(object):
    def uniquePaths(self, m, n):
        # 2D - DP, T(n): O(n.m), S(n): O(n) - no of columns in a row
        row = [1]*n
        for i in range(m-2,-1,-1): # except the bottom row which is all 1's
            newRow = [1]*n
            for j in range(n-2,-1,-1): #except the last Col which is all 1's
                newRow[j] = newRow[j+1]+row[j] # right value + down value of previous row 
            row = newRow
        return  row[0]

