class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        for i in range(len(s)):
            m=len(s)
            for j in range(len(s)):
                if s[j]==c:
                    m=min(m,abs(i-j))
            a.append(m)
        return a