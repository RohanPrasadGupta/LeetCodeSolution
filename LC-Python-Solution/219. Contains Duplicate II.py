class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        nMap = {}
        for i,num in enumerate(nums):

            if ((num in nMap)and(abs(i-nMap[num])<=k)):
                return True

            nMap[num] = i
        
        return False





        