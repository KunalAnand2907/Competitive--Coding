class Solution(object):
    def spiralOrder(self, matrix):
        # T(n): O(n.m), S(n):O(1)
        k=0 # w.r.t 
        l=0
        ans=[]
        m=len(matrix) # rows
        n=len(matrix[0]) # cols
        while(k<m and l<n):
            for i in range(l,n): # first wrt a 1st row
                 ans.append(matrix[k][i])
            k+=1
            for i in range(k,m): # then wrt last column
                 ans.append(matrix[i][n-1])
            n-=1
            if (k<m): # last row
                for i in range(n-1,l-1,-1):
                      ans.append(matrix[m-1][i])
                m-=1
            if(l<n):
                for i in range(m-1,k-1,-1):
                     ans.append(matrix[i][l])
                l+=1
        return ans
                
            
        
        
        