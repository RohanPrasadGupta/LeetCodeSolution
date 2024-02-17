class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = l + ((r-l)//2)

            if((m+1 == len(nums) or nums[m]!=nums[m+1]) and (m-1<0 or nums[m]!=nums[m-1])):
                return nums[m]
            
            leftSize = m-1 if nums[m] ==nums[m-1] else m

            if leftSize%2:
                r = m - 1
            else:
                l = m + 1









        