/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function (n) {
  let count = 0;
  let i = 1;

  while (i <= n) {
    count += 1;
    n -= i;
    i += 1;
  }
  return count;
};
