class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sortedList=sorted(nums)
        return sortedList[len(sortedList)//2]