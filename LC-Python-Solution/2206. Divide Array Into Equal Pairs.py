def divideArray(nums):
    #print(nums)
    resDic = dict()
    
    for i in nums:
        if i in resDic:
            resDic[i]+=1
        else:
            resDic[i] = 1
    
    #print(resDic)
    
    for ele,val in resDic.items():
        if val % 2 !=0:
            return False
    return True
        
    
nums = [3,2,3,2,2,2]
divideArray(nums)

nums = [1,2,3,4]
divideArray(nums)