/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
  let m;
  if (s.lenght % 2 === 0) {
    m = s.lenght / 2;
  } else {
    m = Math.floor(s.length / 2) + 1;
  }
  let l = 0;
  let r = s.length - 1;

  while (l <= r) {
    [s[l], s[r]] = [s[r], s[l]];
    l += 1;
    r -= 1;
  }
};
