class Solution:
    def numRescueBoats(self, p: List[int], lim: int) -> int:
        p.sort()
        boat=0
        l=0
        r=len(p)-1
        while l<=r:
            res=lim-p[r]
            r-=1
            boat+=1
            if l<=r and res>=p[l]:
                l+=1
        return boat
