/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  const rows = Array(9)
    .fill(null)
    .map(() => new Set());
  const cols = Array(9)
    .fill(null)
    .map(() => new Set());
  const square = Array(9)
    .fill(null)
    .map(() => new Set());

  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      let num = board[i][j];

      if (num === ".") {
        continue;
      }

      if (
        rows[i].has(num) ||
        cols[j].has(num) ||
        square[Math.floor(i / 3) * 3 + Math.floor(j / 3)].has(num)
      ) {
        return false;
      }

      rows[i].add(num);
      cols[j].add(num);
      square[Math.floor(i / 3) * 3 + Math.floor(j / 3)].add(num);
    }
  }
  return true;
};
