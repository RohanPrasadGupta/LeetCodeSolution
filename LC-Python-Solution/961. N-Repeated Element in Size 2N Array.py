def repeatedNTimes(nums):
    from collections import Counter
    num_dic = Counter(nums)
    #print(num_dic)
    
    res_num = 0
    max_count = 0 
    for num , count in num_dic.items():
        #print(num,count)
        #print(type(num),type(count))
        if count >= max_count:
            #print(count,num,'IF')
            max_count = count
            res_num = num
    
    print(res_num)
    
    
nums = [5,1,5,2,5,3,5,4]
repeatedNTimes(nums)


nums = [2,1,2,5,3,2]
repeatedNTimes(nums)

nums = [5,1,5,2,5,3,5,4]
repeatedNTimes(nums)