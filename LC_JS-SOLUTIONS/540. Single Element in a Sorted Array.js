/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function (nums) {
  let l = 0;
  let r = nums.length - 1;

  while (l <= r) {
    let m = l + Math.floor((r - l) / 2);

    if (
      (m - 1 < 0 || nums[m] != nums[m - 1]) &&
      (m + 1 === nums.length || nums[m] != nums[m + 1])
    ) {
      return nums[m];
    }

    let leftSide = nums[m] === nums[m - 1] ? m - 1 : m;

    if (leftSide % 2) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
};
