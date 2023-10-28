def maxProduct(nums):
    #print(nums)
    res = []
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            #print(nums[i],nums[j])
            res.append((nums[i]-1)*(nums[j]-1))
    
    #print(res)
    return (max(res))
    

# ANOTHER SOLUTION

def maxProduct(nums):
    return (max([(nums[i]-1)*(nums[j]-1) for i in range(0,len(nums)-1) for j in range(i+1,len(nums))]))
    

nums = [3,4,5,2]
maxProduct(nums)

nums = [1,5,4,5]
maxProduct(nums)


nums = [3,7]
maxProduct(nums)

