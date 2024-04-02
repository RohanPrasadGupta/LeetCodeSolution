/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  let sDic = {};
  let tDic = {};

  for (let i = 0; i < s.length; i++) {
    let charS = s[i];
    let charT = t[i];
    if (charS in sDic) {
      if (sDic[charS] !== charT) return false;
    } else {
      sDic[charS] = charT;
    }

    if (charT in tDic) {
      if (tDic[charT] !== charS) return false;
    } else {
      tDic[charT] = charS;
    }
  }

  return true;
};
