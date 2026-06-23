class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c=0
        co=0
        while c<len(g) and co<len(s):
            if s[co]>=g[c]:
                c+=1
            co+=1
        return c