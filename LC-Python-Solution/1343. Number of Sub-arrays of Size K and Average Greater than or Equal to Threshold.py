class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        count = 0
        curSum = sum(arr[:k-1])

        for i in range(len(arr)-k+1):
            curSum+=arr[i + k - 1]
            if curSum/k>=threshold:
                count+=1
            
            curSum-= arr[i]
        
        return count
        
        
        
        #  68 TEST pased from the below code but not Optimal Soultion
        # count = 0
        # for i in range(len(arr)-k+1):
        #     if (sum(arr[i:i+k])/k) >= threshold:
        #         count +=1
        # return count

        #  66 TEST pased from the below code but not Optimal Soultion
        # res = []
        # l = 0
        # r = k-1

        # while r<len(arr):
        #     if sum(arr[l:r+1])/k >= threshold:
        #         res.append(arr[l:r])
        #     l+=1
        #     r+=1
        
        # return len(res)

        