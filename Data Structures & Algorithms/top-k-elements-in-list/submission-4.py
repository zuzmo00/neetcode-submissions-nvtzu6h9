class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            dic.setdefault(num,0)
            dic[num]+=1
        eredmeny=[key for key,v in sorted(dic.items(),key=lambda x:x[1],reverse=True)[:k]]
        return eredmeny

            