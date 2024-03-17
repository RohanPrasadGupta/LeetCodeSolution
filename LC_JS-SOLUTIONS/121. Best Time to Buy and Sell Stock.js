/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  if (prices.length === 0) {
    return 0;
  }

  let maxProfit = 0;
  let minProfit = prices[0];

  for (let price of prices) {
    minProfit = Math.min(minProfit, price);
    profit = price - minProfit;
    maxProfit = Math.max(profit, maxProfit);
  }

  return maxProfit;
};
