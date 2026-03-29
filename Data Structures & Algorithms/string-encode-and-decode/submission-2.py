class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string="#".join(word.replace("#", "##") for word in strs)
        return [encoded_string]

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find(":", i)
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res