def maximumCount(nums):
    print(nums)
    posCount = 0
    negCount = 0
    
    for i in nums:
        if i<0:
            negCount+=1
        elif i>0:
            posCount+=1
    
    return max(negCount,posCount)

nums = [-2,-1,-1,1,2,3]
maximumCount(nums)

nums = [-3,-2,-1,0,0,1,2]
maximumCount(nums)

nums = [5,20,66,1314]
maximumCount(nums)