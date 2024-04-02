class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        sDic = {}
        tDic = {}

        for i in range(len(s)):
            charS = s[i]
            charT = t[i]

            if charS in sDic:
                if sDic[charS] != charT:
                    return False
            else:
                sDic[charS] = charT

            if charT in tDic:
                if tDic[charT] != charS:
                    return False
            else:
                tDic[charT] = charS
        
        return True

        

