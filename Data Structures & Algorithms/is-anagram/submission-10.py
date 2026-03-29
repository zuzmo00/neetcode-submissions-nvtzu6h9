class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        for letra in s:
            if s.count(letra)!=t.count(letra):
                return False
        return True