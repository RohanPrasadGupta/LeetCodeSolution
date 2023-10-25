def uniqueOccurrences(arr):
    #print(arr)
    
    arrDic = dict()
    for i in arr:
        if i not in arrDic:
            arrDic[i] = 1
        else:
            arrDic[i]+=1
    
    #print(arrDic)
    arrSet = set()
    
    for item,value in arrDic.items():
        if value in arrSet:
            return False
        else:
            arrSet.add(value)
    
    return True
    
    
    
arr = [1,2,2,1,1,3]
uniqueOccurrences(arr)

arr = [1,2]
uniqueOccurrences(arr)


arr = [-3,0,1,-3,1,1,1,-3,10,0]
uniqueOccurrences(arr)