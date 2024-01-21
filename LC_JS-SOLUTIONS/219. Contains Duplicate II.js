/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  nMap = {};

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in nMap && Math.abs(i - nMap[nums[i]]) <= k) {
      return true;
    }

    nMap[nums[i]] = i;
  }

  return false;
};
