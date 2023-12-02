class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backTrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return
            
            for i in range(start,len(candidates)):
                if candidates[i] > target:
                    continue
                
                path.append(candidates[i])
                backTrack(i,target-candidates[i],path)
                path.pop()


        result = []
        candidates.sort()
        backTrack(0,target,[])
        return result

        


        