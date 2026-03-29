class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[i] = nums[i]
        for i in range(len(nums)):
            dif = target - nums[i]
            found_index = next((k for k, v in dic.items() if v == dif), None)
            if found_index is not None and found_index != i:
                return sorted([i, found_index])