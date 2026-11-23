class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,num in enumerate(nums):
            if num in dic:
                return [dic[num],i]
            needed=target-num
            dic[needed]=i
