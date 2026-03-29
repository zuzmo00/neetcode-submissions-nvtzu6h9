class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        seta=set(nums)
        return target in seta