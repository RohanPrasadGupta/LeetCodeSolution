words = ["cd", "ac", "dc", "ca", "zz"]

revSet = set()
count = 0

for word in words:
    #print(word,word[::-1])
    revWord = word[::-1]
    
    if revWord in revSet:
        #print('if run')
        revSet.remove(revWord)
        count+=1
        #print(count)
    else:
        #print('else run')
        revSet.add(word)

print(count)
print(revSet)    