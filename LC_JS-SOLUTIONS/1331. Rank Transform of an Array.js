/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    let temp = [...new Set(arr)].sort(function(a,b){return a-b});
    let resDic = {};
    temp.forEach((num, index) => {
        resDic[num] = index + 1;
    });
    return arr.map(num => resDic[num]);
    
};