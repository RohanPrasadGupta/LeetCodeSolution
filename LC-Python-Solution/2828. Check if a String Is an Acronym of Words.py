def isAcronym(words,s):
    sLen = len(s)
    wLen = len(words)
    
    if sLen != wLen:
        return False
    i = 0
    for word in words:
        if word[0] != s[i]:
            return False
        
        i+=1
    return True
    
    
    
words = ["alice","bob","charlie"]
s = "abc"
isAcronym(words,s)
    
words = ["an","apple"]
s = "a"
isAcronym(words,s)


words = ["never","gonna","give","up","on","you"]
s = "ngguoy"
isAcronym(words,s)