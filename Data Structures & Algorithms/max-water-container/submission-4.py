class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        res=0

        while l<r:
            if h[l]<h[r]:
                prod=h[l]*(r-l)
                l+=1
            elif h[l]>h[r]:
                prod=h[r]*(r-l)
                r-=1
            else:
                prod=h[r]*(r-l)
                r-=1
            res=max(prod,res)
        return res