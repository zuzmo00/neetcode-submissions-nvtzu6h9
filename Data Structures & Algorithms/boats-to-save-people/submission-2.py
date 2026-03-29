class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        res = 0
        l, r = 0, len(p)-1
        while l<=r:
            remain=limit-p[r]
            r-=1
            res+=1
            if l<=r and remain>=p[l]:
                l+=1


        
        return res