class Solution:
    def maxProfit(self, p: List[int]) -> int:
        sum=0
        l=0
        r=1
        sum=0
        while r<len(p):
            if p[l]<p[r]:
                profit=p[r]-p[l]
                sum=max(sum,profit)
            else:
                l=r
            r+=1

        return sum