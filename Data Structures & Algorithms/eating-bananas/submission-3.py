class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        l=1
        r=max(p)
        res=r
        while l<=r:
            m=l+(r-l)//2
            hour=0
            for i in p:
                hour+=(i+m-1)//m
            if hour<=h:
                res=m
                r=m-1
            else:
                l=m+1
        return res

            