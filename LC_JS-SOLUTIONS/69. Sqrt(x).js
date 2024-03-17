/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  let l = 0;
  let r = x;
  let res = 0;

  while (l <= r) {
    let m = Math.floor((l + r) / 2);

    if (m ** 2 > x) {
      r = m - 1;
    } else if (m ** 2 < x) {
      l = m + 1;
      res = m;
    } else {
      return m;
    }
  }
  return res;
};
