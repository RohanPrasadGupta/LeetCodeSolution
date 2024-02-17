/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
  let arr = [];
  let l = 0;
  let r = nums.length - 1;

  while (l <= r) {
    if (nums[l] * nums[l] < nums[r] * nums[r]) {
      arr.unshift(nums[r] * nums[r]);
      r -= 1;
    } else {
      arr.unshift(nums[l] * nums[l]);
      l += 1;
    }
  }
  return arr;
};
