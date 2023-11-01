def nextGreaterElement(nums1,nums2):
    numDict ={}
    for i in range(0,len(nums2)):
        grtNumFound = False
        for j in range(i+1,len(nums2)):
            if nums2[j]>nums2[i]:
                numDict[nums2[i]] = nums2[j]
                grtNumFound = True
                break
        if not grtNumFound:
            numDict[nums2[i]] = -1
    
    for i in range(0,len(nums1)):
        if nums1[i] in numDict:
            nums1[i] = numDict[nums1[i]]
    
    return nums1
    
    