def findWords(words):
    #print(words)
    def isInSameRow(word):
        rows = ["qwertyuiop" ,"asdfghjkl","zxcvbnm"]
        for row in rows:
            if all(char.lower() in row for char in word):
                return True
        return False
        
    return [word for word in words if isInSameRow(word)]


words = ["Hello","Alaska","Dad","Peace"]
findWords(words)

words = ["omk"]
findWords(words)


words = ["adsdf","sfd"]
findWords(words)