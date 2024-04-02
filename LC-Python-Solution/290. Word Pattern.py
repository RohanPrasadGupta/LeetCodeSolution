class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        sArr = s.split(" ")
        wordDic = {}
        charDic = {}

        if(len(sArr)!=len(pattern)):
            return False
    
        for [char,word] in zip(pattern,sArr):
            if char not in charDic:
                if word in wordDic:
                    return False
                
                charDic[char] = word
                wordDic[word] = char
            
            elif charDic[char]!=word or wordDic[word]!=char:
                return False
        
        return True
            


