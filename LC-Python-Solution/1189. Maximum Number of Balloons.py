def charCounter(text):
    neededText = {'b':1, 'a':1,'l':2, 'o':2,'n':1}
    genText = {}
              
    for char in text:
        if char in genText:
            genText[char] +=1
        else:
            genText[char] = 1

    print("genText: ",genText)

    word_count = float('inf')

    for char, count in neededText.items():
        #print(char,count)
        if char in genText:
            word_count = min(word_count,genText[char]//count)
        else:
            return 0
    
    return word_count
    
    
text = "lonbalxballpoon"
charCounter(text)




