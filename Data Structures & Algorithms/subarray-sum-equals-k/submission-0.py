class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        res=0
        dic={0:1}
        for i in nums:
            sum+=i
            diff=sum-k
            res+=dic.get(diff,0)
            dic[sum]=1+dic.get(sum,0)
        return res