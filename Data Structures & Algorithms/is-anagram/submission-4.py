class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_a = {}
        dict_b = {}
        for i in s:
            if i in dict_a:
                dict_a[i] += 1
            else:
                dict_a[i] = 1
        for i in t:
            if i in dict_b:
                dict_b[i] += 1
            else:
                dict_b[i] = 1
        tartalmaz=dict_a.items()==dict_b.items()
        return tartalmaz
        