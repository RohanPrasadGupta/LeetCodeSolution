def sortString(s):
    from collections import Counter
    count_alpha = Counter(s)
    print(count_alpha)
    
    unique_char = sorted(set(s))
    #print(unique_char)
    res = []
    
    while count_alpha:
        for char in unique_char:
            if char in count_alpha:
                res.append(char)
                count_alpha[char]-= 1
                if count_alpha[char] == 0:
                    del count_alpha[char]
        
        for char in unique_char[::-1]:
            if char in count_alpha:
                res.append(char)
                count_alpha[char]-=1
                if count_alpha[char] == 0:
                    del count_alpha[char]
        
    print(res)
    return ''.join(res)

s = "aaaabbbbcccc"
sortString(s)


s = "rat"
sortString(s)