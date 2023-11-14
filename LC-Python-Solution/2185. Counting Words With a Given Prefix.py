def prefixCount(words,pref):
    n = len(pref)
    count = 0
    for word in words:
        temp = word[0:n]
        if temp == pref:
            count +=1
    
    return count