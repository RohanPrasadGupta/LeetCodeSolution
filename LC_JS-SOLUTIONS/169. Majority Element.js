/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  let numDic = {};
  for (let num of nums) {
    if (num in numDic) {
      numDic[num] += 1;
    } else {
      numDic[num] = 1;
    }
  }

  let maxItem = 0;
  let maxVal = 0;

  for (const [item, val] of Object.entries(numDic)) {
    if (val > maxVal) {
      maxVal = Math.max(maxVal, val);
      maxItem = item;
    }
  }
  return maxItem;
};
