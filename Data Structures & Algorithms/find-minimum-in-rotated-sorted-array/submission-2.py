class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        res=nums[0]
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
                res=min(res,nums[m])
        return res
            
