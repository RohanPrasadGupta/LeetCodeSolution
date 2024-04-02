class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        for num1 in nums1:
            maxNum = 0
            numFound = False
            for i in range(len(nums2)):
                if nums2[i] == num1:
                    numFound = True
                if num1 < nums2[i] and numFound:
                    maxNum = nums2[i]
                    res.append(maxNum)
                    break
            if maxNum == 0:
                res.append(-1)
        
        return res




        