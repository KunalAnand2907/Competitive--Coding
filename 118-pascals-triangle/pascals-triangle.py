class Solution(object):
    def generate(self, numRows):
        # Dp 2D, T(n): O(n**2), S(n): O(n**2)
        res= [[1]] # base case
        for i in range(numRows-1): # for each R in res, neglecting the 1st Row
            tmp = [0]+res[-1]+[0] # modified first row
            row = [] # row that will take columns of next row
            for j in range(len(res[-1])+1): # the length o fnext ow will be +1 the len of previous row
                row.append(tmp[j]+tmp[j+1])
            res.append(row) # add the next row
        return res
