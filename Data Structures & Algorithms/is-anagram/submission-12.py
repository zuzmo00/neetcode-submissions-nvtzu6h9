class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicA={}
        dicB={}
        if len(s)!=len(t):
            return False
        for i in s:
            dicA[i]=dicA.setdefault(i,0)+1

        for i in t:
            dicB[i]=dicB.setdefault(i,0)+1
        if dicA==dicB:
            return True
        return False