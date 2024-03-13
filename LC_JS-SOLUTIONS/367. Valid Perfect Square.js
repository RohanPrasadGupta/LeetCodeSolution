/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
  if (num === 1) {
    return true;
  }

  for (let i = 1; i < Math.floor(num / 2) + 1; i++) {
    if (i * i === num) {
      return true;
    } else if (i * i > num) {
      return false;
    }
  }
  return false;
};

// ANOTHER SOLUTION

/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
  let l = 1;
  let r = num;

  while (l <= r) {
    let m = Math.floor((l + r) / 2);
    if (m * m < num) {
      l = m + 1;
    } else if (m * m > num) {
      r = m - 1;
    } else {
      return true;
    }
  }
  return false;
};
