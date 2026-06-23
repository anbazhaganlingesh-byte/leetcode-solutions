class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m=Counter(text)
        a=m['b']
        b=m['a']
        c=m['l']//2
        d=m['o']//2
        e=m['n']
        return min(a,b,c,d,e)