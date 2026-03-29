class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=[".","?","!",",","'",":"]
        original =[x.upper() for x in s if x not in c and x!=" "]
        reversedWord="".join(reversed(s))
        reversedList=[x.upper() for x in reversedWord if x not in c and x!=" "]
        if reversedList==original:
            return True
        else:
            return False