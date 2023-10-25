class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
    
        for i in range(len(nums)-2):
            left , right = i+1, len(nums)-1
        
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
            
                if abs(curr_sum-target) < abs(closest_sum-target):
                    closest_sum = curr_sum
        
                if curr_sum < target:
                    left +=1
                else:
                    right -=1
        
            if closest_sum == target:
                return closest_sum
    
        return closest_sum
    

