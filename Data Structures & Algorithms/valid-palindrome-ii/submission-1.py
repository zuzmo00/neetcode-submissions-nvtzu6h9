class Solution:
    def validPalindrome(self, s: str) -> bool:
    
        def isPolindrome(l,r):
            while l<r:
                if s[l].lower()!=s[r].lower():
                    return False
                l+=1
                r-=1
            return True
        l=0
        r=len(s)-1

        while l<r:
            if s[l].lower()!=s[r].lower():
                return (isPolindrome(l+1,r)or
                        isPolindrome(l,r-1))
            l+=1
            r-=1
        return True