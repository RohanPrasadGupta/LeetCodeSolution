class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = [word for word in s.split(" ") if len(word)>0 ]

        return (len(res[-1]))


