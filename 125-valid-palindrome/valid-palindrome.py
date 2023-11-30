class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1:
        # import re
        # s  = re.sub('[^0-9A-Za-z]','',s)
        # return s == s[::-1]
        l,r=0,len(s)-1
        while(l<r):
            # only check whether it is not accept letter,number, incr & decr the l,r pointer
            if not(s[l].isalnum()):
                l+=1
            elif not(s[r].isalnum()):
                r-=1
            else:
                # 
                if s[l].lower()!=s[r].lower():
                    return False
                l+=1
                r-=1
        # edge case when empty or 1 length
        return True
        