def distinctDifferenceArray(nums):
    res = []
    for i in range(0,len(nums)):
        lset = set(nums[0:i+1])
        rset = set(nums[i+1:])
        print("left",len(lset),'right',len(rset))
        res.append(len(lset)-len(rset))
        
    return (res)

        
nums = [3,2,3,4,2]
distinctDifferenceArray(nums)

nums = [1,2,3,4,5]
distinctDifferenceArray(nums)