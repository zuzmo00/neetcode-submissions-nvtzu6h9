class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        length=len(nums)//3
        for i in nums:
            dic[i]=dic.setdefault(i,0)+1
        return [k for k,v in dic.items() if v>length]

        