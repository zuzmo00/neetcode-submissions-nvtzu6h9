class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        res=0
        dic={0:1}
        for i in nums:
            sum+=i
            diff=sum-k
            if diff in dic:
                res+=dic[diff]
            dic[sum]=dic.setdefault(sum,0)+1
        return res
        