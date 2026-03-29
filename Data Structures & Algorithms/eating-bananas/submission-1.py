class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        l=1
        r=max(p)
        value=p[len(p)-1]

        while l<=r:
            hours=0
            m=l+(r-l)//2
            for i in p:
                hours+=math.ceil(i/m)
            if hours<=h:
                value=m
                r=m-1
            else:
                l=m+1
        return value
            