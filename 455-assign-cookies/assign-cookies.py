class Solution(object):
    def findContentChildren(self, g, s):
        # 2 Pointers( Greedy Approach - maximize the content childrens), T(n): O(nlogn), S(n): O(1) -  we can't combine 2 cookies at diff position and content the greed of a child

        # 1.) sort the both arrays so that we can max the number of childrens
        g.sort()
        s.sort()
        i,j=0,0
        while( i<len(g) and j<len(s)):
            if(g[i]<=s[j]):
                i+=1
                j+=1
            else: # g[i]>s[i] - we can't content the child as we are not assigning the enough size of cookie
                j+=1
        return i

        