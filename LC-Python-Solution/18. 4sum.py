def fourSum(nums,target):
    #print(nums,target)
    res = []
    nums.sort()
    for i in range(0,len(nums)-3):
        for j in range(i+1,len(nums)-2):
            for k in range(j+1,len(nums)-1):
                for l in range(k+1,len(nums)):
                    if sum([nums[i],nums[j],nums[k],nums[l]]) == target:
                        subArr = [nums[i],nums[j],nums[k],nums[l]]
                        #subArr.sort()
                        print(subArr,"SUM :",sum(subArr))
                        if subArr not in res:
                            res.append(subArr)
    
    return(res)
    
    

    #OPTIMIZED SOLUTION 
    # def fourSum(nums,target):
    # #print(nums,target)
    # nums.sort()
    # res = set()
    # for i in range(0,len(nums)-3):
    #     for j in range(i+1,len(nums)-2):
    #         left = j+1
    #         right = len(nums)-1
    #         while left < right:
    #             curSum = nums[i]+nums[j]+nums[left]+nums[right]
            
    #             if curSum == target:
    #                 res.add((nums[i],nums[j],nums[left],nums[right]))
    #                 left+=1
    #                 right-=1
    #             elif curSum<target:
    #                 left+=1
    #             else:
    #                 right-=1
    
    # return res
                


nums = [1,0,-1,0,-2,2]
target = 0
fourSum(nums,target)


nums = [2,2,2,2,2]
target = 8
fourSum(nums,target)

nums =[-5,5,4,-3,0,0,4,-2]
target = 4 
fourSum(nums,target)


nums = [-493,-487,-480,-464,-456,-449,-445,-439,-437,-427,-415,-403,-400,-398,-372,-349,-347,-332,-330,-324,-287,-282,-273,-254,-249,-243,-220,-219,-217,-217,-214,-199,-198,-170,-153,-150,-143,-136,-113,-93,-91,-88,-87,-78,-58,-58,-55,-51,-49,-42,-38,-36,-26,0,13,28,54,61,85,90,90,111,118,136,138,167,170,172,195,198,205,209,241,263,290,302,324,328,347,359,373,390,406,417,435,439,443,446,464,465,468,484,486,492,493]
target = -4437
fourSum(nums,target)

nums = [-500,-499,-496,-467,-467,-465,-461,-460,-456,-456,-447,-426,-425,-401,-377,-367,-344,-338,-332,-329,-328,-294,-281,-262,-256,-224,-196,-192,-171,-161,-151,-138,-130,-109,-109,-107,-104,-101,-97,-96,-90,-78,-76,-70,-28,-23,-4,30,39,46,60,80,97,120,172,183,194,197,206,238,242,243,252,303,338,341,349,362,366,367,372,393,400,403,406,411,416,454,457,460,497]
target = -1963
fourSum(nums,target)