class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s)==0:
            return True

        res = ''
        for i in range(0,len(s)):
            if s[i].isalpha() or s[i].isdigit():
                res+=s[i]
        
        return(res.lower() == res[::-1].lower())
        


        