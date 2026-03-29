class Solution:
    def maxProfit(self, p: List[int]) -> int:
        sum=0
        for i in range(len(p)-1):
            if p[i+1]>p[i]:
                sum+=p[i+1]-p[i]
        return sum