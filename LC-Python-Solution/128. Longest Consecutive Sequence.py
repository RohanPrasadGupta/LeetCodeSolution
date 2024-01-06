class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longCount = 0
        curCount = 0

        for num in nums:
            if num-1 not in numSet:
                curNum = num
                curCount = 1

                while curNum+1 in numSet:
                    curNum+=1
                    curCount+=1
            
            longCount = max(longCount,curCount)
        

        return longCount











        