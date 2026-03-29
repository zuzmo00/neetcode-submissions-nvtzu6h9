class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        l=1
        r=max(p)
        res=0
        value=p[len(p)-1]

        while l<=r:
            res=0
            m=l+(r-l)//2
            for i in p:
                res+=math.ceil(i/m)
            if res<=h:
                value=m
                r=m-1
            else:
                l=m+1
        return value
            