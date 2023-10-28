def countGoodSubstrings(s):
    #print(s)
    res = []
    for i in range(0,len(s)-2):
        #print(s[i:i+3])
        if s[i] != s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]:
            res.append(s[i:i+3])
    
    #print(res)
    return len(res)
        
    
    
s = "xyzzaz"
countGoodSubstrings(s)

s = "aababcabc"
countGoodSubstrings(s)