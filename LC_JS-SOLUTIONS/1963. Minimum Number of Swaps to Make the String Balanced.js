/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function (s) {
  let bracCount = 0;
  let Count = 0;

  for (let brac of s) {
    if (brac === "]") bracCount += 1;
    else bracCount -= 1;
    Count = Math.max(bracCount, Count);
  }

  return Math.floor((Count + 1) / 2);
};
