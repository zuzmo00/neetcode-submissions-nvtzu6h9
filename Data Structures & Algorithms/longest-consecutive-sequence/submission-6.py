class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # Átalakítjuk halmazzá a gyors kereséshez
        longest = 0

        for n in num_set:
            # Csak akkor kezdünk el számolni, ha n az első elem (n-1 nincs benne)
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
                
        return longest