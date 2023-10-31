def maximizeSum(nums,k):
    maxEle = max(nums)
    score = 0
    prevEle = maxEle
    
    for i in range (0,k):
        score+= prevEle
        prevEle+=1
    
    return score
    
    
    
    
nums = [5,5,5]
k = 2
maximizeSum(nums,k)

nums = [1,2,3,4,5]
k = 3
maximizeSum(nums,k)