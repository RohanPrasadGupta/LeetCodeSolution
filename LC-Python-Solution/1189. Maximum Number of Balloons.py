class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        charNeed = {"b":1,"a":1,"l":2,"o":2,"n":1}
        charGain ={}

        wordFormed = float('inf')

        for char in text:
            if char in charGain:
                charGain[char]+=1
            else:
                charGain[char] = 1
        
        for item,val in charNeed.items():
            if item in charGain:
                wordFormed = min(wordFormed , charGain[item]//val)
            else:
                return 0
        
        return wordFormed


        
        