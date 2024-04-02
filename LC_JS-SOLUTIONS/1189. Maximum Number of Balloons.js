/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function (text) {
  let charNeed = { b: 1, a: 1, l: 2, o: 2, n: 1 };
  let charGain = {};
  let wordCount = Infinity;

  for (let char of text) {
    if (char in charGain) charGain[char] += 1;
    else charGain[char] = 1;
  }

  for (let [item, count] of Object.entries(charNeed)) {
    if (item in charGain) {
      wordCount = Math.min(wordCount, Math.floor(charGain[item] / count));
    } else {
      return 0;
    }
  }
  return wordCount;
};
