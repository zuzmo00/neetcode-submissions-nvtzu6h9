class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=0
        while l<r:
            
            if nums[l]<nums[r]:
                prod = nums[l]* (r - l)
                l+=1

            else:
                prod = nums[r] * (r - l)
                r-=1
            if res<prod:
                res=prod
        return res

