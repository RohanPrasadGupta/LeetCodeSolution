def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ('')
    
    
words = ["abc","car","ada","racecar","cool"]
firstPalindrome(words)

words = ["notapalindrome","racecar"]
firstPalindrome(words)

words = ["def","ghi"]
firstPalindrome(words)