class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1l = 0
        w2l = 0
        s = ''

        while w1l < len(word1) and w2l<len(word2):
            s = s + word1[w1l] + word2[w2l]
            w1l+=1
            w2l+=1

        while w1l<len(word1):
            s = s + word1[w1l]
            w1l+=1 
        
        while w2l < len(word2):
            s = s + word2[w2l]
            w2l+=1 
        
        return s






        