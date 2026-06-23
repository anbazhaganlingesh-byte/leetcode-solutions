class Solution:
    def processStr(self, s: str) -> str:
        m=""
        for i in s:
            if i.isalpha():
                m+=i
            elif i=="#":
                m=m+m
            elif i=="%":
                m=m[::-1]
            else:
                m=m[:-1]
        return m