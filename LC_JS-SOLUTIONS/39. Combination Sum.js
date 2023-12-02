/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {


    function backTrack(start,target,path){

        if (target == 0){
            result.push([...path])
            return
        }

        for(let i = start; i<candidates.length; i++){

            if (candidates[i]>target){
                continue
            }

            path.push(candidates[i])
            backTrack(i, target-candidates[i],path)
            path.pop()

        }

    }



    let result = []
    candidates.sort((a,b)=>a-b)
    backTrack(0,target,[])
    return result



    
};