class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedList=sorted(set(nums))
        count=0
        longestCount=0
        for i in range(1,len(sortedList)):
            if sortedList[i]-1==sortedList[i-1]:
                count+=1
                if longestCount<count:
                    longestCount=count
            else:
                count=0
        if longestCount!=0:
            longestCount+=1
        if len(sortedList)==1:
            longestCount+=1
        return longestCount