/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function (arr, k, threshold) {
  let count = 0;
  let curSum = 0;

  for (let i = 0; i < k; i++) {
    curSum += arr[i];
  }

  for (let i = 0; i <= arr.length - k; i++) {
    if (i > 0) {
      curSum = curSum + arr[i + k - 1] - arr[i - 1];
    }

    if (curSum / k >= threshold) {
      count += 1;
    }
  }

  return count;
};
