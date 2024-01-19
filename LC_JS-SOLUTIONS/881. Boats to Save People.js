/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function (people, limit) {
  people.sort((a, b) => a - b);
  let n = people.length;
  let l = 0;
  let r = people.length - 1;
  let res = [];

  while (l <= r) {
    if (people[r] === limit) {
      res.push([people[r]]);
      r -= 1;
    } else if (people[l] + people[r] <= limit) {
      res.push([people[l], people[r]]);
      l += 1;
      r -= 1;
    } else if (people[l] + people[r] > limit && people[r] < limit) {
      res.push([people[r]]);
      r -= 1;
    }
  }
  return res.length;
};
