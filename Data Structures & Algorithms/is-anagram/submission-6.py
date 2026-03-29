class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}


        for betu in s:
            hash_map[betu] = hash_map.get(betu, 0) + 1

        for betu in t:
            if betu not in hash_map:
                return False
            hash_map[betu] -= 1
        

            if hash_map[betu] < 0:
                return False


        return all(ertek == 0 for ertek in hash_map.values())
        