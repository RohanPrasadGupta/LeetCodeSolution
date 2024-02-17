/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  let l = 1;
  let r = Math.max(...piles);
  let res = r;

  function canEat(cap) {
    let hour = 0;

    for (let ban of piles) {
      hour += Math.floor((ban + cap - 1) / cap);
    }
    return hour <= h;
  }

  while (l <= r) {
    let cap = l + Math.floor((r - l) / 2);

    if (canEat(cap)) {
      res = Math.min(cap, res);
      r = cap - 1;
    } else {
      l = cap + 1;
    }
  }
  return res;
};
