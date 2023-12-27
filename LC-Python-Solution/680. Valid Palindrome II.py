class Solution:
    def validPalindrome(self, s: str) -> bool:

        lp = 0
        rp = len(s)-1

        while lp<rp:
            if s[lp] != s[rp]:
                skipL = s[lp+1 :rp+1]
                skipR = s[lp:rp]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            lp+=1
            rp-=1
        
        return True

        