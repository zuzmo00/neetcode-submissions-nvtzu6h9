class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket={}

        for word in strs:
            temp="".join(sorted(word))

            if temp not in bucket:
                bucket[temp]=[]
            bucket[temp].append(word)
        final=list(bucket.values())
        return final