class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums=set(nums)
        longest=0
        current=0
        if not nums:return 0
        for i in nums:
            current=0
            if i-1 not in setNums:
                while i+1 in setNums:
                    i+=1
                    current+=1
                if longest<current:
                    longest=current

        return longest+1
                    
                