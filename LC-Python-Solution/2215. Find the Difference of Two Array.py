def diffTwoArray(nums1,nums2):
    res = []
    temp = []
    for i in range(0,len(nums1)):
        if nums1[i] not in nums2 and nums1[i] not in temp:
            temp.append(nums1[i])
    res.append(temp)
    temp = []
    for i in range(0,len(nums2)):
        if nums2[i] not in nums1 and nums2[i] not in temp:
            temp.append(nums2[i])
    res.append(temp)

    return(res)

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
diffTwoArray(nums1,nums2)



#ANOTHER SOLUTION

def diffTwoArray(nums1,nums2):
    return list(set(x for x in nums1 if x not in nums2)),list(set(x for x in nums2 if x not in nums1))


nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
diffTwoArray(nums1,nums2)