class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(2):
            for a in range(n):
                ans.append(nums[a])
        return ans