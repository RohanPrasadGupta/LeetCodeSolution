def mergeArrays(nums1,nums2):
    #print(nums1,nums2)
    resDic = dict()
    for sArr in nums1:
        key = sArr[0]
        value = sArr[1]
        #print(sArr[i],sArr[j])
        if key not in resDic:
            resDic[key] = value
        else:
            resDic[key]+=value
    
    for sArr in nums2:
        key = sArr[0]
        value = sArr[1]
        if key in resDic:
            resDic[key] +=value
        else:
            resDic[key] = value
    
    resDic = dict(sorted(resDic.items()))

    return ([[key,value] for key,value in resDic.items()])


nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
mergeArrays(nums1,nums2)


nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
mergeArrays(nums1,nums2)