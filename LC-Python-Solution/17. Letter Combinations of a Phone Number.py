class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numDic = {'2':'abc',
              '3':'def',
              '4':'ghi',
              '5':'jkl',
              '6':'mno',
              '7':'pqrs',
              '8':'tuv',
              '9':'wxyz'
             }
        
        res = []

        def backtrack(i,subChar):
            if len(subChar) == len(digits):
                res.append(subChar)
                return
            
            for char in numDic[digits[i]]:
                backtrack(i+1, subChar + char)

        if digits:
            backtrack(0,'')
        
        return res

        