class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        # i want to map the price to an index and then minus the largest index from the smallest index

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                res = max(res, profit)
        return res




        

        