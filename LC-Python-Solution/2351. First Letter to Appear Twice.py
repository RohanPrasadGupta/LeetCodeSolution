def repeatedCharacter(s):
    print(s)
    sDic = dict()
    for i in s:
        if i not in sDic:
            sDic[i] = 1
        else:
            return i

s = "abccbaacz"
repeatedCharacter(s)

s = "abcdd"
repeatedCharacter(s)