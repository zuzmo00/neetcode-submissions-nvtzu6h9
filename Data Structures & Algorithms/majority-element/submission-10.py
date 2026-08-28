class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        number=nums[0]
        for i in nums:
            if i== number:
                count=count+1
            elif number!=i:
                count=count-1
            if count==0:
                number=i
                count+=1
        return number