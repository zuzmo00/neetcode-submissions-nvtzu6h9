class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number=count=0

        for i in nums:
            if count==0:
                number=i
            count+=(1 if number==i else -1)
        return number