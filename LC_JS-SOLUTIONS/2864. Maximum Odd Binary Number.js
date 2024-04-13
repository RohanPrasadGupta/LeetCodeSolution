/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function (s) {
  numOne = (s.match(/1/g) || []).length;
  numZero = (s.match(/0/g) || []).length;
  res = "1".repeat(numOne - 1) + "0".repeat(numZero) + "1";
  return res;
};
