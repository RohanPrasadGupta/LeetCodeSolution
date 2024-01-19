class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        maxEle = -1

        for i in range( n-1 , -1 , -1 ):
            curEle = arr[i]
            arr[i] = maxEle
            maxEle = max(curEle , maxEle)

        
        return arr
    
    
        