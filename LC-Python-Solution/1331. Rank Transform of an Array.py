class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        resDic = { num: index+1 for index,num in enumerate(temp)}
        return [resDic[num] for num in arr]
    


# OPTIMIZE VERSION OF THE BELWO CODE

# temp = sorted(set(arr))
#         resDic = {}
#         for num in arr:
#             if num not in resDic:
#                 resDic[num] = temp.index(num)+1

#         for i in range(0,len(arr)):
#             arr[i] = resDic[arr[i]]
        
#         return arr