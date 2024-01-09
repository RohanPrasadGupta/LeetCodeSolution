/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function (nums, target) {
  nums.sort((a, b) => a - b);

  let left = 0;
  let right = nums.length - 1;
  let power = [1];
  let result = 0;
  let pow = 10 ** 9 + 7;

  for (let i = 1; i < nums.length; i++) {
    power.push((power[power.length - 1] * 2) % pow);
  }

  while (left <= right) {
    if (nums[left] + nums[right] > target) {
      right -= 1;
    } else {
      result += power[right - left];
      left += 1;
    }
  }

  return result % pow;
};
