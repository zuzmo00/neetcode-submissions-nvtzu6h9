class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dica={}
        dicb={}
        for i in s:
            dica[i]=dica.setdefault(i,0)+1
        for i in t:
            dicb[i]=dicb.setdefault(i,0)+1
        return dica==dicb

        