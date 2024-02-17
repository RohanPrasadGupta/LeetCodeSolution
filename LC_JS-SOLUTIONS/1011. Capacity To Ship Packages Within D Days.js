/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function (weights, days) {
  let l = Math.max(...weights);
  let r = weights.reduce((acc, val) => acc + val, 0);
  let res = r;

  while (l <= r) {
    let cap = l + Math.floor((r - l) / 2);

    function isCapacity(cap) {
      let ship = 1;
      let capacity = cap;

      for (let i = 0; i < weights.length; i++) {
        if (capacity - weights[i] < 0) {
          ship += 1;
          capacity = cap;
        }
        capacity -= weights[i];
      }

      return ship <= days;
    }

    if (isCapacity(cap)) {
      res = Math.min(res, cap);
      r = cap - 1;
    } else {
      l = cap + 1;
    }
  }

  return res;
};
