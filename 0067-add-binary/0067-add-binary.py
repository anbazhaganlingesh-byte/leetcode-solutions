class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sval=int(a,2)+int(b,2)
        return bin(sval)[2:]