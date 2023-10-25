def findTheDifference(s,t):
    print(s,t)
    s_dict = dict()
    t_dict = dict()
    
    for i in s:
        if i not in s_dict:
            s_dict[i] = 1
        else:
            s_dict[i]+=1
    for i in t:
        if i not in t_dict:
            t_dict[i] = 1
        else:
            t_dict[i]+=1
    
    print(s_dict,t_dict)
    
    for char,count in t_dict.items():
        if char not in s_dict or count > s_dict[char]:
            return char


s = "abcd"
t = "abcde"
findTheDifference(s,t)

s ="a"
t ="aa"
findTheDifference(s,t)


#ANOTHER SOLUTION

from collections import Counter
def findTheDifference(s,t):
    s_dict = Counter(s)
    t_dict = Counter(t)
    print(s_dict,t_dict)
    
    for char,count in t_dict.items():
        if char not in s_dict or count > s_dict[char]:
            return char
