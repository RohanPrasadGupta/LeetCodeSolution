class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        s = list(s)

        for i in range(0,len(s),2*k):
            start = i
            end = min(i+k,len(s))
            s[start:end] =  reversed(s[start:end])
        
        return (''.join(s))





        