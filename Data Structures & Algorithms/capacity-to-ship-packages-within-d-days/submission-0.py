class Solution:
    def shipWithinDays(self, w: List[int], d: int) -> int:
        l=max(w)
        r=sum(w)
        res=r
        def canShip(m):
            ship=1
            capacity=m
            for i in w:
                if capacity-i<0:
                    ship+=1
                    capacity=m
                capacity-=i
            return ship<=d




        while l<=r:
            m=l+(r-l)//2
            if canShip(m):
                res=(min(res,m))
                r=m-1
            else:
                l=m+1
        return res
