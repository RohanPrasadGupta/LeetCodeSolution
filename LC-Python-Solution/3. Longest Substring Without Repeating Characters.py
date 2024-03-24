class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cSet = set()
        l = 0
        res = 0

        for i in range(len(s)):
            while s[i] in cSet:
                cSet.remove(s[l])
                l+=1
            
            cSet.add(s[i])
            res = max(res,i-l+1)
        
        return res









        