class Solution(object):
    def isSubsequence(self, s, t):
        # Base case 1: when subsequence is empty
        if len(s)==0:
            return True
        # Base case 2: when string is empty or sub seq len >string len
        elif len(t)==0 or len(s)>len(t):
            return False
        else:
            sub=0
            for i in range(len(t)):
                if sub<len(s):
                    #print(s[sub])
                    if s[sub]==t[i]:
                        sub+=1
            return sub==len(s) # at the end if sub index equals len(s) - it matches - true
            # Another Method
    #         if len(t)==0:
    #     return True
    # elif len(s)==0 or len(t)>len(s):
    #     return False
    # i1,i2=0,0
    # while(i1<len(s) and i2<len(t)):
    #     if s[i1]!=t[i2]:
    #         i2+=1
    #         continue # below st are not executed, we go to next iter 
    #     i1+=1
    #     i2+=1
    # return i1==len(s)
            
                
        