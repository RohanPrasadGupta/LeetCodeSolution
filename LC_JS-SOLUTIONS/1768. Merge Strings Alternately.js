/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  w1l = 0;
  w2l = 0;
  let s = "";

  while (w1l < word1.length && w2l < word2.length) {
    s = s + word1[w1l] + word2[w2l];
    w1l += 1;
    w2l += 1;
  }

  while (w1l < word1.length) {
    s = s + word1[w1l];
    w1l += 1;
  }

  while (w2l < word2.length) {
    s = s + word2[w2l];
    w2l += 1;
  }

  return s;
};
