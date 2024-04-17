/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function (s) {
  let res = new Set();
  let left = new Set();
  let right = new Map();

  for (let char of s) {
    right.set(char, (right.get(char) || 0) + 1);
  }
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    right.set(char, right.get(char) - 1);
    if (right.get(char) === 0) {
      right.delete(char);
    }

    for (let j = 0; j < 26; j++) {
      const c = String.fromCharCode("a".charCodeAt(0) + j);
      if (left.has(c) && right.has(c)) {
        res.add(s[i] + c);
      }
    }
    left.add(char);
  }
  return res.size;
};
