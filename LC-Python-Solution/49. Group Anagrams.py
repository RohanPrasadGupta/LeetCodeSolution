class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        strDic = {}

        for subStr in strs:
            if(''.join(sorted(subStr)) not in strDic):
                strDic[''.join(sorted(subStr))] = [subStr]
            
            else:
                strDic[''.join(sorted(subStr))].append(subStr)
        
        for index,key in enumerate(strDic):
            res.append(strDic[key])
        
        return res





        