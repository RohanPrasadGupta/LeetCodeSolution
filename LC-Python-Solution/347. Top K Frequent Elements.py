class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numDic = {}
        for num in nums:
            if num not in numDic:
                numDic[num] = 1
            else:
                numDic[num]+=1
        
        sortedNumDic = dict(sorted( numDic.items() , key = lambda x:x[1], reverse = True))

        res = []

        for index, key in enumerate(sortedNumDic):
            res.append(key)
        
        return (res[:k])











        