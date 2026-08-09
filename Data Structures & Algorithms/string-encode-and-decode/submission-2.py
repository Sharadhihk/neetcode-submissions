class Solution:

    def encode(self, strs: List[str]) -> str:
        newS=""
        for s in strs:
            newS+=str(len(s))+"#"+s
        return newS

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = s.find("#", i)

            length = int(s[i:j])

            oldS = s[j+1:j+1+length]
            strs.append(oldS)

            i = j + 1 + length

        return strs
