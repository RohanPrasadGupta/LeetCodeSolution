class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    #print([nums[i],nums[j],nums[k]])
                    if (nums[i]< nums[j]) and (nums[j] - nums[i] == diff) and (nums[j]< nums[k]) and (nums[k] - nums[j] == diff):
                        res.append([nums[i],nums[j],nums[k]])
        
        return(len(res))