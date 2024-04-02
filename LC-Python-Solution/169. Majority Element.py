class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        numDic = {}

        for num in nums:
            if num in numDic:
                numDic[num] +=1
            else:
                numDic[num] = 1
        
        maxItem = 0
        maxVal = 0

        for item,val in numDic.items():
            if (val > maxVal):
                maxVal = max(maxVal,val)
                maxItem = item
        
        return maxItem


        