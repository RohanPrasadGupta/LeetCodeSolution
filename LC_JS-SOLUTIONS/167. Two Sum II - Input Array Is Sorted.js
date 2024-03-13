/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  let l = 0;
  let r = numbers.length - 1;
  let res = [];

  while (l < r) {
    if (numbers[l] + numbers[r] > target) {
      r -= 1;
    } else if (numbers[l] + numbers[r] < target) {
      l += 1;
    } else if (numbers[l] + numbers[r] === target) {
      res.push(l + 1);
      res.push(r + 1);
      return res;
    }
  }
};
