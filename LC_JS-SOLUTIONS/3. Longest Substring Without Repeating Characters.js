/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let cSet = new Set();
  let l = 0;
  let res = 0;

  for (let i = 0; i < s.length; i++) {
    while (cSet.has(s[i])) {
      cSet.delete(s[l]);
      l += 1;
    }
    cSet.add(s[i]);
    res = Math.max(res, i - l + 1);
  }

  return res;
};
