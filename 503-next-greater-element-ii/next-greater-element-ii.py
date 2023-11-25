class Solution(object):
    def nextGreaterElements(self, A):
        # T(n):O(2n+2n), S(n)-O(n) - 2 pass Solution, Monotonic Decreasing Stack, while entering from last to first Mono Inc Stack
        st, ng = [], [-1]*len(A)
        n = len(A)
        for i in range((2*n)-1,-1,-1):
            while(st!=[] and st[-1]<=A[i%n]):
                st.pop()
            if (i<n and st!=[]):
                ng[i%n] = st[-1]
            st.append(A[i%n])
        return ng
        