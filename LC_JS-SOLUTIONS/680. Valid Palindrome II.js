/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function (s) {
  let lp = 0;
  let rp = s.length - 1;

  while (lp < rp) {
    if (s[lp] !== s[rp]) {
      let skipL = s.slice(lp + 1, rp + 1);
      let skipR = s.slice(lp, rp);

      return (
        skipL === skipL.split("").reverse().join("") ||
        skipR === skipR.split("").reverse().join("")
      );
    }
    lp += 1;
    rp -= 1;
  }
  return true;
};
