class Solution:
    def shipWithinDays(self, w: List[int], s: int) -> int:
        l=max(w)
        r=sum(w)
        res=r
        def canShip(m):
            ship=1
            cap=m
            for i in w:
                if cap-i<0:
                    ship+=1
                    cap=m
                cap=cap-i
            return ship<=s

        while l<=r:
            m=l+(r-l)//2
            if canShip(m):
                r=m-1
                res=m

            else:
                l=m+1
        return res

