/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {

    let res = {}
    for(let i=0; i<nums.length; i++){
        if (!(nums[i] in res)){

            res[nums[i]] = 1
        }
        else{
            return true
        }
    }
    return false
    
};