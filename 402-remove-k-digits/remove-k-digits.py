class Solution(object):
    def removeKdigits(self, num, k):
         # Stack
        st=[]
        for c in num:
            # move from left to right and check the below cond
            # if found any prev greater than the current so will remove it
            while(k>0 and st and st[-1]>c):
                k-=1
                st.pop()
            st.append(c)
        # when an increasing order string is found while loop doesn't runs
        st = st[0:len(st)-k]
        # we have list of strings
        res = ''.join(st)
        # chechk for any leading zero's if there
        return str(int(res)) if res else "0"