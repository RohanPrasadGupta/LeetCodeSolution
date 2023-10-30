def separateDigits(nums):
    #print(nums)
    res = []
    for num in nums:
        if num < 10:
            res.append(num)
        
        else:
            temp = str(num)
            tempRes = [int(char) for char in temp]
            for i in tempRes:
                res.append(i)
        
    
    print(res)


# ANOTHER CODE
def separateDigits(nums):
    #print(nums)
    res = []
    for num in nums:
        for char in str(num):
            res.append(int(char))
    return res


nums = [13,25,83,77]
separateDigits(nums)



nums = [7,1,3,9]
separateDigits(nums)
