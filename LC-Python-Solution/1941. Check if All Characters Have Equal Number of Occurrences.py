def equalOcc(s):
    occTable = dict()
    for i in s:
        if i in occTable:
            occTable[i]+=1
        else:
            occTable[i] = 1

    #print(occTable)
    val = occTable[s[0]]
    #print(val)
    if len(occTable)==1:
        return True
    for data,value in occTable.items():
        #print(data,value)
        if value != val:
            return False
    return True

s = "wzkpzzwzpzkwkpkppzkppkpkwwkzzzwwpwwk"
equalOcc(s)

s = "aaabb"
equalOcc(s)

s = "abacbc"
equalOcc(s)


s = "vvvvvvvvvvvvvvvvvvv"
equalOcc(s)