def maxNumber(nums):
    #print(nums)
    numDic = {}
    remCount = 0
    pairCount = 0

    for num in nums:
        if num in numDic:
            numDic[num] +=1
        else:
            numDic[num] = 1

    for num in nums:
        if numDic[num]>=2:
            pairCount +=1
            numDic[num]-=2
    for count in numDic.values():
        remCount+=count

    return([pairCount,remCount])  
    
    
   
               
    
nums = [1,3,2,1,3,2,2]
maxNumber(nums)

nums = [1,1]
maxNumber(nums)

nums = [0]
maxNumber(nums)