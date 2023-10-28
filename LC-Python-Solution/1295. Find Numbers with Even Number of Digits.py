def findNumbers(nums):
    #print(nums)
    res = []
    for num in nums:
        if len(str(num)) %2==0:
            res.append(num)
    
    return len(res)

#ANOTHER SOLUTION


def findNumbers(nums):
    return len([num for num in nums if len(str(num))%2==0])
    

nums = [12,345,2,6,7896]
findNumbers(nums)

nums = [555,901,482,1771]
findNumbers(nums)