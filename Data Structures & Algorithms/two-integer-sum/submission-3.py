class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        
        for i in range(len(nums)):
            result=target-nums[i]
            if result in dic:
                return [dic[result],i]
            dic[nums[i]]=i
            
