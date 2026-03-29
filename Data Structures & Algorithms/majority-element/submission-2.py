class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number=nums[0]
        count=0
        for i in nums:
            if i==number:
                count+=1
            else:
                count-=1
            if count==0:
                number=i
                count+=1
        return number