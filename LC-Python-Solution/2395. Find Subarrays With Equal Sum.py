def subArray(nums):
    #print(nums)
    res = []
    for i in range(0,len(nums)-1):
        if nums[i]+nums[i+1] in res:
            return True
        else:
            res.append(nums[i]+nums[i+1])
    
    return False
            

nums = [4,2,4]
subArray(nums)