class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)
        for i in nums:
            count[i]+=1

            if len(count)<=2:
                continue
            newCounter=defaultdict(int)
            for k,v in count.items():
                if v>1:
                    newCounter[k]=v-1
                count=newCounter
        res=[]
        for i in count:
            if nums.count(i)>len(nums)//3:
                res.append(i)
        return res
        
