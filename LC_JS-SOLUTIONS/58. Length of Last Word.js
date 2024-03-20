/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  res = s.split(" ").filter((word) => word.length > 0);

  return res[res.length - 1].length;
};
