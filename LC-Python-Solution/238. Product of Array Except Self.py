class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = [1] * n
        left = [1] * n
        right = [1] * n

        l = 1
        for i in range(1,n):
            l = l *nums[i-1]
            left[i] = l
        
        r = 1
        for j in range(n-2,-1,-1):
            r = r*nums[j+1]
            right[j] = r
        
        for i in range(0,n):
            res[i] = left[i] * right[i]
        
        return res









