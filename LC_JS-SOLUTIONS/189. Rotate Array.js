/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  if (nums.length == k || nums.length == 1) {
    return nums;
  }

  k = k % nums.length;

  let l = 0;
  let r = nums.length - 1;
  while (l < r) {
    [nums[l], nums[r]] = [nums[r], nums[l]];
    l += 1;
    r -= 1;
  }

  let l2 = 0;
  let r2 = k - 1;
  while (l2 < r2) {
    [nums[l2], nums[r2]] = [nums[r2], nums[l2]];
    l2 += 1;
    r2 -= 1;
  }

  let l3 = k;
  let r3 = nums.length - 1;
  while (l3 < r3) {
    [nums[l3], nums[r3]] = [nums[r3], nums[l3]];
    l3 += 1;
    r3 -= 1;
  }
};
