class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if numbers[i] in dic:
                for a in range(len(numbers)):
                    if numbers[a] ==diff:
                        return[a+1,i+1]
            dic[diff]=1

