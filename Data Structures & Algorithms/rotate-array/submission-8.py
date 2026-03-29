class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        def rotator(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        rotator(0,len(nums)-1)
        rotator(0,k-1)
        rotator(k,len(nums)-1)

        

    