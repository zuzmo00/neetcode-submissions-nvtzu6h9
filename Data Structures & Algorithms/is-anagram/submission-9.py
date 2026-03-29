class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_s = list(s)
        for char in t:
            try:
                string_s.remove(char)
            except ValueError:
                return False
        if len(string_s) == 0:
            return True
        else:
            return False
