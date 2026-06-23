class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        v=0
        for i in s+t:
            v^=ord(i)
        return chr(v)