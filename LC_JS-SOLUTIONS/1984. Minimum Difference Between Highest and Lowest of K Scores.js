/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function (nums, k) {
  nums.sort((a, b) => a - b);
  let l = 0;
  let r = k - 1;
  res = Infinity;

  while (r < nums.length) {
    res = Math.min(res, nums[r] - nums[l]);
    r = r + 1;
    l = l + 1;
  }

  return res;
};
