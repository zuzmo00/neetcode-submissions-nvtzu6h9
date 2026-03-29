class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        res=''
        while l<len(word1) or r<len(word2):
            if len(word1)==l:
                while r<len(word2):
                    res+=word2[r]
                    r+=1
                return res
            if len(word2)==r:
                while l<len(word1):
                    res+=word1[l]
                    l+=1
                return res
            res+=word1[l]
            res+=word2[r]
            
            l+=1
            r+=1
        return res