/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var largestLocal = function (grid) {
  let n = grid.length;
  let res = [];

  for (let i = 0; i < n - 2; i++) {
    let row = [];
    for (let j = 0; j < n - 2; j++) {
      let subArr = [];
      for (let k = 0; k < 3; k++) {
        subArr.push(grid[i + k].slice(j, j + 3));
      }
      let maxValue = Math.max(...subArr.flat());
      row.push(maxValue);
    }
    res.push(row);
  }
  return res;
};
