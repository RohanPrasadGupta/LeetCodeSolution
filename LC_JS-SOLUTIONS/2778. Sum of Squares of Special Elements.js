/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfSquares = function(nums) {

    let n = nums.length
    res = 0
    for(let i=0;i<nums.length;i++ ){
        if(n%(i+1)==0){
            res+=nums[i]**2
        }
    }

    return res


    
};