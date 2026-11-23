class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dica={}
        dicb={}

        for i in s:
            if i in dica:
                dica[i]+=1
            else:
                dica.setdefault(i,1)
        for i in t:
            if i in dicb:
                dicb[i]+=1
            else:
                dicb.setdefault(i,1)
        if dica==dicb:
            return True
        return False