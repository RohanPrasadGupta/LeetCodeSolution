/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let l = 0;
  let r = height.length - 1;
  let maxArea = 0;
  while (l < r) {
    let area = (r - l) * Math.min(height[l], height[r]);
    maxArea = Math.max(area, maxArea);

    if (height[l] < height[r]) {
      l += 1;
    } else {
      r -= 1;
    }
  }

  return maxArea;
};
