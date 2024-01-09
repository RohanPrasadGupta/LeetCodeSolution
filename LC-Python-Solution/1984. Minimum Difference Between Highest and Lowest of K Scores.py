class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        res = float("inf")
        l = 0 
        r = k-1
        
        while r<len(nums):
            res = min(res, nums[r] - nums[l] )
            l= l + 1
            r= r + 1
        
        return res






        