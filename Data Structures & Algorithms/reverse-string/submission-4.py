class Solution:
    def reverseString(self, s: List[str]) -> None:
        b=len(s)-1
        a=0
        for i in range(len(s)):
            a=s[i]
            s[i]=s[b]
            s[b]=a
            b-=1
            if i>=b:
                break
            

        