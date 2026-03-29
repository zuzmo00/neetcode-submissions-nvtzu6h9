class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        osszeg=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                osszeg+=(prices[i+1])-prices[i]
        return osszeg
