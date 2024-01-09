/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function (nums) {
  if (nums.includes(0)) {
    return 0;
  }

  return Math.sign(nums.reduce((acc, num) => acc * num, 1));
};
