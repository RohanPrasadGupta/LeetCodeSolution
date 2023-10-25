from collections import Counter 
def findSpecialInteger(arr):
    print(arr)
    numDic = Counter(arr)
    print(numDic)
    res = 0
    comp = 0
    
    for ele,value in numDic.items():
        print(ele,value)
        if value>comp:
            res = ele
            comp = value
    
    return res
    
    
    
arr = [1,2,2,6,6,6,6,7,10]
findSpecialInteger(arr)


arr = [1,1]
findSpecialInteger(arr)

arr =[6700,8858,8858,8858,8858]
findSpecialInteger(arr)