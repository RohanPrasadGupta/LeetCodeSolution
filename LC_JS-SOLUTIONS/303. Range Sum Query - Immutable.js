/**
 * @param {number[]} nums
 */
var NumArray = function (nums) {
  this.prefix = [];
  let cur = 0;

  for (let num of nums) {
    cur += num;
    this.prefix.push(cur);
  }
};

/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function (left, right) {
  let rightSum = this.prefix[right];
  let leftSum = left > 0 ? this.prefix[left - 1] : 0;
  return rightSum - leftSum;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
