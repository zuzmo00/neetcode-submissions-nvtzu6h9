class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        res=0
        while l<=r:
            m=l+(r-l)//2
            num=m*m
            if num==x:
                return m
            elif num >x:
                r=m-1
            else:
                l=m+1
                res=m
        return res