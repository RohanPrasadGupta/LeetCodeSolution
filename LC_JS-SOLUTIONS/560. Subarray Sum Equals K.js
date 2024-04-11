/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  let count = 0;
  let prefixSum = new Map();
  let currSum = 0;
  prefixSum.set(0, 1);

  for (let i = 0; i < nums.length; i++) {
    currSum += nums[i];
    if (prefixSum.has(currSum - k)) {
      count += prefixSum.get(currSum - k);
    }
    prefixSum.set(currSum, (prefixSum.get(currSum) || 0) + 1);
  }
  return count;
};
