def uniqueMorseRepresentations(words):
    M_letter = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    res = ''
    hTable = {}

    for i in range(0,len(words)):
        print(words[i])
        for char in words[i]:
            #print(char)
            res += M_letter[ord(char)- ord('a')]
    
        if res in hTable:
            hTable[res] +=1
        else:
            hTable[res] = 1
        
        res = ''

    #print(res)
    print(hTable)
    return(len(hTable))    


words = ["a"]
uniqueMorseRepresentations(words)


#ANOTHER SOLUTION
def uniqueMorseRepresentations(words):
    M_letter = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    Uni_word = set()
    
    for word in words:
        #print(word)
        Mcode = ''.join(M_letter[ord(char)-ord('a')] for char in word)
        #print(Mcode)
        Uni_word.add(Mcode)
    
    print(Uni_word)
    print(len(Uni_word))
    

    


words = ["gin","zen","gig","msg"]
uniqueMorseRepresentations(words)