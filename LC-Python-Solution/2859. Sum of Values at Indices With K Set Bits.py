def sumIndicesWithKSetBits(nums,k):
    dicArr = dict()
    for i in range (0,len(nums)):
        num = bin(i).replace('0b','')
        count = 0
        for j in num:
            if j == '1':
                count +=1
        dicArr[i] = count
    res = 0
    for num,val in dicArr.items():
        #print(num,val)
        if val == k:
            res = res + nums[num]
    return res

nums = [5,10,1,5,2]
k = 1
sumIndicesWithKSetBits(nums,k)

nums = [4,3,2,1]
k = 2
sumIndicesWithKSetBits(nums,k)