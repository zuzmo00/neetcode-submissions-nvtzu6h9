class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l=0
        res=0
        for r in range(len(p)):
            if p[r]>p[l]:
                profit=p[r]-p[l]
                res=max(res,profit)
            else:
                l=r
        return res