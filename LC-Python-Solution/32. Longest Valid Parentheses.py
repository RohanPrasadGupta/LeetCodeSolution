class Solution:
    def longestValidParentheses(self, s: str) -> int:

        maxLen = 0
        bracStack = []
        bracStack.append(-1)

        for i in range(len(s)):
            if s[i] == "(":
                bracStack.append(i)
            else:
                if bracStack:
                    bracStack.pop()
                    if bracStack:
                        maxLen = max(maxLen, i - bracStack[-1])
                    else:
                        bracStack.append(i)
        
        return maxLen
        
        