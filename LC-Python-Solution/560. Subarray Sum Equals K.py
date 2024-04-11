class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        curSum = 0
        numDic = {0:1}

        for num in nums:
            curSum += num

            if curSum-k in numDic:
                count+=numDic[curSum-k]
            
            numDic[curSum] = numDic.get(curSum,0)+1
        
        return count

        